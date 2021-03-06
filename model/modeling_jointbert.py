import torch
import torch.nn as nn
from torchcrf import CRF
from transformers import BertModel, BertConfig
from .module import IntentClassifier, SlotClassifier


class JointBert(nn.Module):
    def __init__(self, args, intent_label_lst, slot_label_lst):
        super().__init__()
        self.args = args
        self.num_intent_labels = len(intent_label_lst)
        self.num_slot_labels = len(slot_label_lst)
        self.config = BertConfig.from_pretrained(
            args.pretrained_path,
            from_tf=False,
            output_hidden_states=True,
            return_dict=True,
        )
        self.bert_model = BertModel.from_pretrained(
            args.pretrained_path, config=self.config
        )
        self.model_type = type(self.bert_model).__name__.replace("Model", "").lower()
        self.n_hiddens = args.n_hiddens
        self.intent_classifier = IntentClassifier(
            self.config.hidden_size * max(1, self.n_hiddens),
            self.num_intent_labels,
            args.dropout_rate,
        )

        self.slot_classifier = SlotClassifier(
            self.config.hidden_size,
            self.num_intent_labels,
            self.num_slot_labels,
            self.args.use_intent_context_concat,
            self.args.use_intent_context_attention,
            self.args.max_seq_len,
            self.args.attention_embedding_size,
            args.dropout_rate,
        )

        if args.use_crf:
            self.crf = CRF(num_tags=self.num_slot_labels, batch_first=True)

    def forward(
        self,
        input_ids,
        attention_mask,
        token_type_ids,
        intent_label_ids,
        slot_labels_ids,
    ):

        if self.model_type in [
            "t5",
            "distilbert",
            "electra",
            "mbart",
            "bart",
            "xlm",
            "xlnet",
            "camembert",
            "longformer",
        ]:
            outputs = self.bert_model(
                input_ids,
                attention_mask=attention_mask,
            )
        else:
            outputs = self.bert_model(
                input_ids,
                attention_mask=attention_mask,
                token_type_ids=token_type_ids,
            )

        # sequence_output, pooled_output, (hidden_states), (attentions)

        sequence_output = outputs["last_hidden_state"]

        if self.n_hiddens >= 1:
            hidden_states_key = "hidden_states"
            if "bart" in self.model_type:
                hidden_states_key = "decoder_hidden_states"
            pooled_output = torch.cat(
                [
                    outputs[hidden_states_key][-i][:, 0, :]
                    for i in range(self.n_hiddens)
                ],
                axis=-1,
            )
        elif self.n_hiddens == 0:
            pooled_output = outputs["pooler_output"]
        else:
            token_embeddings = outputs["last_hidden_state"]
            input_mask_expanded = (
                attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
            )
            pooled_output = torch.sum(
                token_embeddings * input_mask_expanded, 1
            ) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

        intent_logits = self.intent_classifier(pooled_output)
        if not self.args.use_attention_mask:
            tmp_attention_mask = None
        else:
            tmp_attention_mask = attention_mask

        if self.args.embedding_type == "hard":
            hard_intent_logits = torch.zeros(intent_logits.shape)
            for i, sample in enumerate(intent_logits):
                max_idx = torch.argmax(sample)
                hard_intent_logits[i][max_idx] = 1
            slot_logits = self.slot_classifier(
                sequence_output, hard_intent_logits, tmp_attention_mask
            )
        else:
            slot_logits = self.slot_classifier(
                sequence_output, intent_logits, tmp_attention_mask
            )

        total_loss = 0
        # 1. Intent Softmax
        if intent_label_ids is not None:
            if self.num_intent_labels == 1:
                intent_loss_fct = nn.MSELoss()
                intent_loss = intent_loss_fct(
                    intent_logits.view(-1), intent_label_ids.view(-1)
                )
            else:
                intent_loss_fct = nn.CrossEntropyLoss()
                intent_loss = intent_loss_fct(
                    intent_logits.view(-1, self.num_intent_labels),
                    intent_label_ids.view(-1),
                )
            total_loss += self.args.intent_loss_coef * intent_loss

        # 2. Slot Softmax
        if slot_labels_ids is not None:
            if self.args.use_crf:
                slot_loss = self.crf(
                    slot_logits,
                    slot_labels_ids,
                    mask=attention_mask.byte(),
                    reduction="mean",
                )
                slot_loss = -1 * slot_loss  # negative log-likelihood
            else:
                slot_loss_fct = nn.CrossEntropyLoss(ignore_index=self.args.ignore_index)
                # Only keep active parts of the loss
                if attention_mask is not None:
                    active_loss = attention_mask.view(-1) == 1
                    active_logits = slot_logits.view(-1, self.num_slot_labels)[
                        active_loss
                    ]
                    active_labels = slot_labels_ids.view(-1)[active_loss]
                    slot_loss = slot_loss_fct(active_logits, active_labels)
                else:
                    slot_loss = slot_loss_fct(
                        slot_logits.view(-1, self.num_slot_labels),
                        slot_labels_ids.view(-1),
                    )
            total_loss += (1 - self.args.intent_loss_coef) * slot_loss

        # add hidden states and attention if they are here
        outputs = ((intent_logits, slot_logits),) + outputs[2:]

        outputs = (total_loss,) + outputs

        # (loss), logits, (hidden_states), (attentions) # Logits is a tuple of intent and slot logits
        return outputs
