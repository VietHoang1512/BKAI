datadir=data/syllable-level/test
predictions_dir=predictions
python3 predict.py --input_file $datadir/seq.in \
                              --output_file $predictions_dir/predictions.txt \
                              --result_file $predictions_dir/results.csv \
                              --model_dir outputs/4e-5/0.15/100
