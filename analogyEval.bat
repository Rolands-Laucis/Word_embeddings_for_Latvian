::analogyEval.bat 5 200 3cosmul
@echo off

::set up arguments
set win=%1
set v_size=%2
set eval_method=%3

echo doing word2vec analogy evaluations
python AnalogiesTester.py --model_type word2vec --model_file ../Models/Word2vec_model/word2vec_%win%_%v_size%_sg.wordvectors --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_word2vec_%win%_%v_size%_%eval_method%_top10.txt --gen_output true --eval_method %eval_method% --topn 10 --verbose true
python AnalogiesTester.py --model_type word2vec --model_file ../Models/Word2vec_model/word2vec_%win%_%v_size%_sg.wordvectors --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_word2vec_%win%_%v_size%_%eval_method%.txt --gen_output true --eval_method %eval_method% --topn 1
::echo doing word2vec analogy evaluations on lemmatized corpora
::python AnalogiesTester.py --model_type word2vec --model_file ../Models/Word2vec_model/word2vec_%win%_%v_size%_lem.wordvectors --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_word2vec_%win%_%v_size%_%eval_method%_top10_lem.txt --gen_output true --eval_method %eval_method% --topn 10
::python AnalogiesTester.py --model_type word2vec --model_file ../Models/Word2vec_model/word2vec_%win%_%v_size%_lem.wordvectors --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_word2vec_%win%_%v_size%_%eval_method%_lem.txt --gen_output true --eval_method %eval_method% --topn 1

echo doing FastText analogy evaluations
python AnalogiesTester.py --model_type fasttext --model_file ../Models/FastText_model/fasttext_%win%_%v_size%_sg.wordvectors --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_fasttext_%win%_%v_size%_%eval_method%_top10.txt --gen_output true --eval_method %eval_method% --topn 10
python AnalogiesTester.py --model_type fasttext --model_file ../Models/FastText_model/fasttext_%win%_%v_size%_sg.wordvectors --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_fasttext_%win%_%v_size%_%eval_method%.txt --gen_output true --eval_method %eval_method% --topn 1

echo doing SSG analogy evaluations
python AnalogiesTester.py --model_type ssg --model_file ../Models/SSG_model/ssg_%win%_%v_size%_sg.txt --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_ssg_%win%_%v_size%_%eval_method%_top10.txt --gen_output true --eval_method %eval_method% --topn 10
python AnalogiesTester.py --model_type ssg --model_file ../Models/SSG_model/ssg_%win%_%v_size%_sg.txt --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_ssg_%win%_%v_size%_%eval_method%.txt --gen_output true --eval_method %eval_method% --topn 1

echo analogy evaluations done
pause