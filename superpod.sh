#!/bin/bash  -ex

#SBATCH --job-name=train

#SBATCH --output=/lustre/scratch/client/vinai/users/hoangpv7/implement/BKAI/logs/%A.out

#SBATCH --error=/lustre/scratch/client/vinai/users/hoangpv7/implement/BKAI/logs/%A.err

#SBATCH --partition=research

#SBATCH --gpus=1

#SBATCH --nodes=1

#SBATCH --mem-per-gpu=40G

#SBATCH --cpus-per-gpu=48

#SBATCH --mail-type=all

#SBATCH --mail-user=v.HoangPV7@vinai.io

source /sw/software/miniconda3/bin/activate

conda activate /lustre/scratch/client/vinai/users/hoangpv7/ml

cd /lustre/scratch/client/vinai/users/hoangpv7/implement/BKAI

export lr=4e-5
export s=100
echo "${lr}"

max_seq_len=30

python3 main.py --token_level syllable-level \
                --model_type phobert \
                --model_dir "outputs/$max_seq_len/$lr/.15/$s" \
                --data_dir data \
                --seed $s \
                --do_train \
                --do_eval \
                --max_seq_len $max_seq_len \
                --save_steps 140 \
                --logging_steps 140 \
                --num_train_epochs 100 \
                --tuning_metric semantic_frame_acc \
                --use_intent_context_attention \
                --attention_embedding_size 200 \
                --use_crf \
                --gpu_id 0 \
                --embedding_type soft \
                --intent_loss_coef .15 \
                --pretrained \
                --pretrained_path vinai/phobert-base \
                --learning_rate $lr &
python3 main.py --token_level syllable-level \
                --model_type phobert \
                --model_dir "outputs/$max_seq_len/$lr/.3/$s" \
                --data_dir data \
                --seed $s \
                --do_train \
                --do_eval \
                --max_seq_len $max_seq_len \
                --save_steps 140 \
                --logging_steps 140 \
                --num_train_epochs 100 \
                --tuning_metric semantic_frame_acc \
                --use_intent_context_attention \
                --attention_embedding_size 200 \
                --use_crf \
                --gpu_id 0 \
                --embedding_type soft \
                --intent_loss_coef .3 \
                --pretrained \
                --pretrained_path vinai/phobert-base \
                --learning_rate $lr &
python3 main.py --token_level syllable-level \
                --model_type phobert \
                --model_dir "outputs/$max_seq_len/$lr/.45/$s" \
                --data_dir data \
                --seed $s \
                --do_train \
                --do_eval \
                --max_seq_len $max_seq_len \
                --save_steps 140 \
                --logging_steps 140 \
                --num_train_epochs 100 \
                --tuning_metric semantic_frame_acc \
                --use_intent_context_attention \
                --attention_embedding_size 200 \
                --use_crf \
                --gpu_id 0 \
                --embedding_type soft \
                --intent_loss_coef .45 \
                --pretrained \
                --pretrained_path vinai/phobert-base \
                --learning_rate $lr &
python3 main.py --token_level syllable-level \
                --model_type phobert \
                --model_dir "outputs/$max_seq_len/$lr/.6/$s" \
                --data_dir data \
                --seed $s \
                --do_train \
                --do_eval \
                --max_seq_len $max_seq_len \
                --save_steps 140 \
                --logging_steps 140 \
                --num_train_epochs 100 \
                --tuning_metric semantic_frame_acc \
                --use_intent_context_attention \
                --attention_embedding_size 200 \
                --use_crf \
                --gpu_id 0 \
                --embedding_type soft \
                --intent_loss_coef .6 \
                --pretrained \
                --pretrained_path vinai/phobert-base \
                --learning_rate $lr &
python3 main.py --token_level syllable-level \
                --model_type phobert \
                --model_dir "outputs/$max_seq_len/$lr/.75/$s" \
                --data_dir data \
                --seed $s \
                --do_train \
                --do_eval \
                --max_seq_len $max_seq_len \
                --save_steps 140 \
                --logging_steps 140 \
                --num_train_epochs 100 \
                --tuning_metric semantic_frame_acc \
                --use_intent_context_attention \
                --attention_embedding_size 200 \
                --use_crf \
                --gpu_id 0 \
                --embedding_type soft \
                --intent_loss_coef .75 \
                --pretrained \
                --pretrained_path vinai/phobert-base \
                --learning_rate $lr &
python3 main.py --token_level syllable-level \
                --model_type phobert \
                --model_dir "outputs/$max_seq_len/$lr/.9/$s" \
                --data_dir data \
                --seed $s \
                --do_train \
                --do_eval \
                --max_seq_len $max_seq_len \
                --save_steps 140 \
                --logging_steps 140 \
                --num_train_epochs 100 \
                --tuning_metric semantic_frame_acc \
                --use_intent_context_attention \
                --attention_embedding_size 200 \
                --use_crf \
                --gpu_id 0 \
                --embedding_type soft \
                --intent_loss_coef .9 \
                --pretrained \
                --pretrained_path vinai/phobert-base \
                --learning_rate $lr 


############################################################################################################


# max_seq_len=100

# python3 main.py --token_level syllable-level \
#                 --model_type phobert \
#                 --model_dir "outputs/$max_seq_len/$lr/.15/$s" \
#                 --data_dir data \
#                 --seed $s \
#                 --do_train \
#                 --do_eval \
#                 --max_seq_len $max_seq_len \
#                 --save_steps 140 \
#                 --logging_steps 140 \
#                 --num_train_epochs 100 \
#                 --tuning_metric semantic_frame_acc \
#                 --use_intent_context_attention \
#                 --attention_embedding_size 200 \
#                 --use_crf \
#                 --gpu_id 0 \
#                 --embedding_type soft \
#                 --intent_loss_coef .15 \
#                 --pretrained \
#                 --pretrained_path vinai/phobert-base \
#                 --learning_rate $lr &
# python3 main.py --token_level syllable-level \
#                 --model_type phobert \
#                 --model_dir "outputs/$max_seq_len/$lr/.3/$s" \
#                 --data_dir data \
#                 --seed $s \
#                 --do_train \
#                 --do_eval \
#                 --max_seq_len $max_seq_len \
#                 --save_steps 140 \
#                 --logging_steps 140 \
#                 --num_train_epochs 100 \
#                 --tuning_metric semantic_frame_acc \
#                 --use_intent_context_attention \
#                 --attention_embedding_size 200 \
#                 --use_crf \
#                 --gpu_id 0 \
#                 --embedding_type soft \
#                 --intent_loss_coef .3 \
#                 --pretrained \
#                 --pretrained_path vinai/phobert-base \
#                 --learning_rate $lr &
# python3 main.py --token_level syllable-level \
#                 --model_type phobert \
#                 --model_dir "outputs/$max_seq_len/$lr/.6/$s" \
#                 --data_dir data \
#                 --seed $s \
#                 --do_train \
#                 --do_eval \
#                 --max_seq_len $max_seq_len \
#                 --save_steps 140 \
#                 --logging_steps 140 \
#                 --num_train_epochs 100 \
#                 --tuning_metric semantic_frame_acc \
#                 --use_intent_context_attention \
#                 --attention_embedding_size 200 \
#                 --use_crf \
#                 --gpu_id 0 \
#                 --embedding_type soft \
#                 --intent_loss_coef .6 \
#                 --pretrained \
#                 --pretrained_path vinai/phobert-base \
#                 --learning_rate $lr &
# python3 main.py --token_level syllable-level \
#                 --model_type phobert \
#                 --model_dir "outputs/$max_seq_len/$lr/.9/$s" \
#                 --data_dir data \
#                 --seed $s \
#                 --do_train \
#                 --do_eval \
#                 --max_seq_len $max_seq_len \
#                 --save_steps 140 \
#                 --logging_steps 140 \
#                 --num_train_epochs 100 \
#                 --tuning_metric semantic_frame_acc \
#                 --use_intent_context_attention \
#                 --attention_embedding_size 200 \
#                 --use_crf \
#                 --gpu_id 0 \
#                 --embedding_type soft \
#                 --intent_loss_coef .9 \
#                 --pretrained \
#                 --pretrained_path vinai/phobert-base \
#                 --learning_rate $lr 