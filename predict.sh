datadir=data/test
predictions_dir=predictions
python3 predict.py --input_file $datadir/seq.in \
                              --output_file $predictions_dir/predictions.txt \
                              --result_file $predictions_dir/results.csv \
                              --model_dir outputs/vinai/phobert-base/3e-5/.45/100
