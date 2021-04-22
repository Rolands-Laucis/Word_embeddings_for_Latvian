@echo off

echo doing quick
::python analogyPrep.py --model_type fasttext_original --model_file ../Models/FastText_model/fasttext_baseline_300.vec --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/lv-analogies-fasttext_baseline.txt
python AnalogiesTester.py --model_type fasttext_original --model_file ../Models/FastText_model/fasttext_baseline_300.vec --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_fasttext_baseline_300_CS.txt --gen_output true --eval_method 3cosmul --topn 1
