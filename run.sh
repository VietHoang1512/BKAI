export lr=3e-5
export s=0

max_seq_len=50
model_type=auto
pretrained_path=vinai/phobert-base
testdir=data/test

for c in  .45 .3 .15
do
    for fold in {1..6}
    do
        export MODEL_DIR=outputs/$pretrained_path/$lr/$c/$s/$fold
        echo "${MODEL_DIR}"
        python3 main.py --model_type $model_type \
                        --train_batch_size 64 \
                        --model_dir $MODEL_DIR \
                        --data_dir data/6-folds/fold-$fold \
                        --seed $s \
                        --do_train \
                        --do_eval \
                        --max_seq_len $max_seq_len \
                        --save_steps 50 \
                        --logging_steps 50 \
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
        python3 predict.py --input_file $testdir/seq.in \
                                    --output_file $MODEL_DIR/predictions.txt \
                                    --result_file $MODEL_DIR/results.csv \
                                    --model_dir $MODEL_DIR
        rm -rf $MODEL_DIR/*.bin
    done
done