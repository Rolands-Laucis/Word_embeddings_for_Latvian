@echo off

echo doing quick
::python analogyPrep.py --model_type fasttext_original --model_file ../Models/FastText_model/fasttext_baseline_300.vec --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/lv-analogies-fasttext_baseline.txt
::python AnalogiesTester.py --model_type fasttext_original --model_file ../Models/FastText_model/fasttext_baseline_300.vec --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_fasttext_baseline_300_CS.txt --gen_output true --eval_method 3cosmul --topn 1

python -m spacy train config-pos.cfg --output ../../Models/Spacy_tagger/ssg_5_100_sg_pos --paths.train ./lv_lvtb-ud-train.spacy --paths.dev ./lv_lvtb-ud-dev.spacy

python -m spacy evaluate ..\\..\Models\Spacy_tagger\ssg_5_100_sg_pos\model-best ./lv_lvtb-ud-test.spacy --output ../../datasets/POS/ssg_5_100_sg_pos.json --gold-preproc

