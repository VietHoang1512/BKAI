#As we initialize JointIDSF from JointBERT, user need to train a base model JointBERT first

#Train JointIDSF
export lr=4e-5
export s=100
echo "${lr}"
export MODEL_DIR=outputs

for c in .15 .3 .45 .6 
do
    export MODEL_DIR=$MODEL_DIR"/"$lr"/"$c"/"$s
    echo "${MODEL_DIR}"
    python3 main.py --token_level syllable-level \
                    --model_type phobert \
                    --model_dir $MODEL_DIR \
                    --data_dir data \
                    --seed $s \
                    --do_train \
                    --do_eval \
                    --save_steps 140 \
                    --logging_steps 140 \
                    --num_train_epochs 50 \
                    --tuning_metric mean_intent_slot \
                    --use_intent_context_attention \
                    --attention_embedding_size 200 \
                    --use_crf \
                    --gpu_id 0 \
                    --embedding_type soft \
                    --intent_loss_coef $c \
                    --pretrained \
                    --pretrained_path vinai/phobert-base \
                    --learning_rate $lr
done