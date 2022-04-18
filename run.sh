#As we initialize JointIDSF from JointBERT, user need to train a base model JointBERT first

#Train JointIDSF
export lr=3e-5
export s=100
echo "${lr}"

max_seq_len=50
model_type=auto
pretrained_path=vinai/phobert-base
for c in  .9 .75 .6 .45 .3 .15
do
    export MODEL_DIR=outputs/$pretrained_path
    export MODEL_DIR=$MODEL_DIR"/"$lr"/"$c"/"$s
    echo "${MODEL_DIR}"
    python3 main.py --model_type $model_type \
                    --train_batch_size 32 \
                    --model_dir $MODEL_DIR \
                    --data_dir data \
                    --seed $s \
                    --do_train \
                    --do_eval \
                    --max_seq_len $max_seq_len \
                    --save_steps 140 \
                    --logging_steps 140 \
                    --num_train_epochs 50 \
                    --tuning_metric semantic_frame_acc \
                    --use_intent_context_attention \
                    --attention_embedding_size 200 \
                    --dropout_rate .1 \
                    --n_hiddens 0 \
                    --use_crf \
                    --embedding_type soft \
                    --intent_loss_coef $c \
                    --pretrained \
                    --pretrained_path $pretrained_path \
                    --learning_rate $lr
done