@echo off
echo doing word2vec analogy evaluations
python AnalogiesTester.py --model_type word2vec --model_file ../Models/Word2vec_model/word2vec.wordvectors --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_word2vec_3cosmul_top10.txt --gen_output true --eval_method 3cosmul --topn 10
python AnalogiesTester.py --model_type word2vec --model_file ../Models/Word2vec_model/word2vec.wordvectors --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_word2vec_3cosmul.txt --gen_output true --eval_method 3cosmul --topn 1

echo doing FastText analogy evaluations
python AnalogiesTester.py --model_type fasttext --model_file ../Models/FastText_model/FastText_combined_corp_model.wordvectors --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_fasttext_top10.txt --gen_output true --eval_method 3cosmul --topn 10
python AnalogiesTester.py --model_type fasttext --model_file ../Models/FastText_model/FastText_combined_corp_model.wordvectors --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_fasttext.txt --gen_output true --eval_method 3cosmul --topn 1

echo doing SSG analogy evaluations
python AnalogiesTester.py --model_type ssg --model_file ../Models/SSG_model/ssg_model.txt --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_ssg_top10.txt --gen_output true --eval_method 3cosmul --topn 10
python AnalogiesTester.py --model_type ssg --model_file ../Models/SSG_model/ssg_model.txt --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_ssg.txt --gen_output true --eval_method 3cosmul --topn 1

echo analogy evaluations done
pause