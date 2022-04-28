export lr=3e-5
export s=0

max_seq_len=50
model_type=auto
dropout_rate=.0
num_train_epochs=50
attention_embedding_size=200
pretrained_path=FPTAI/vibert-base-cased
testdir=data/test

for c in  .45 .6 .3 .15 .75 .9
do

    export MODEL_DIR=outputs/$pretrained_path/epoch=$num_train_epochs/lr=$lr/att=$attention_embedding_size/weight=$c/drop=$dropout_rate/seed=$s
    echo "${MODEL_DIR}"
    python3 main.py --model_type $model_type \
                    --train_batch_size 64 \
                    --model_dir $MODEL_DIR \
                    --data_dir data/ \
                    --seed $s \
                    --do_train \
                    --do_eval \
                    --max_seq_len $max_seq_len \
                    --save_steps 140 \
                    --logging_steps 140 \
                    --num_train_epochs $num_train_epochs \
                    --tuning_metric semantic_frame_acc \
                    --use_intent_context_attention \
                    --attention_embedding_size $attention_embedding_size \
                    --dropout_rate $dropout_rate \
                    --n_hiddens 0 \
                    --use_crf \
                    --embedding_type soft \
                    --intent_loss_coef $c \
                    --pretrained \
                    --pretrained_path $pretrained_path \
                    --learning_rate $lr;
    python3 predict.py --input_file $testdir/seq.in \
                                --output_file $MODEL_DIR/predictions.txt \
                                --result_file $MODEL_DIR/results.csv \
                                --model_dir $MODEL_DIR
    rm -rf $MODEL_DIR/*.bin

done