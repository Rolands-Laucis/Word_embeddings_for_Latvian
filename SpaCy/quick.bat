@echo off

::./quick.bat

echo doing quick
::python analogyPrep.py --model_type fasttext_original --model_file ../Models/FastText_model/fasttext_baseline_300.vec --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/lv-analogies-fasttext_baseline.txt
::python AnalogiesTester.py --model_type fasttext_original --model_file ../Models/FastText_model/fasttext_baseline_300.vec --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_fasttext_baseline_300_CS.txt --gen_output true --eval_method 3cosmul --topn 1

::python -m spacy train config-pos.cfg --output ../../Models/Spacy_tagger/ssg_5_100_sg_pos --paths.train ./lv_lvtb-ud-train.spacy --paths.dev ./lv_lvtb-ud-dev.spacy

::python -m spacy evaluate ..\\..\Models\Spacy_tagger\ssg_5_100_sg_pos\model-best ./lv_lvtb-ud-test.spacy --output ../../datasets/POS/ssg_5_100_sg_pos.json --gold-preproc


::python -m spacy convert ..\..\datasets\NER\processed\ner-combined-train.iob ..\..\datasets\NER\processed\ -l lv
::python -m spacy convert ..\..\datasets\NER\processed\ner-combined-dev.iob ..\..\datasets\NER\processed\ -l lv
::python -m spacy convert ..\..\datasets\NER\processed\ner-combined-test.iob ..\..\datasets\NER\processed\ -l lv

::python -m spacy train config-ner.cfg --output ../../Models/Spacy_tagger/word2vec_5_200_sg-ner --paths.train ..\..\datasets\NER\processed\ner-combined-train.spacy --paths.dev ..\..\datasets\NER\processed\ner-combined-dev.spacy --paths.vectors C:\Users\Experimenter\Desktop\BD_Code\Models\Spacy_tagger\word2vec_5_200_sg_vectors

::python -m spacy evaluate ..\..\Models\Spacy_tagger\word2vec_5_200_sg-ner\model-best ..\..\datasets\NER\processed\ner-combined-test.spacy --output ../../datasets/NER/word2vec_5_200_sg-ner.json --gold-preproc
::python -m spacy evaluate ..\..\Models\Spacy_tagger\fasttext_5_200_sg-ner\model-best ..\..\datasets\NER\processed\ner-combined-test.spacy --output ../../datasets/NER/fasttext_5_200_sg-ner.json --gold-preproc
python -m spacy evaluate ..\..\Models\Spacy_tagger\ssg_5_200_sg-ner\model-best ..\..\datasets\NER\processed\ner-combined-test.spacy --output ../../datasets/NER/ssg_5_200_sg-ner.json --gold-preproc
python -m spacy evaluate ..\..\Models\Spacy_tagger\ssg_5_100_sg-ner\model-best ..\..\datasets\NER\processed\ner-combined-test.spacy --output ../../datasets/NER/ssg_5_100_sg-ner.json --gold-preproc
python -m spacy evaluate ..\..\Models\Spacy_tagger\ng2v_5_200_sg-ner\model-best ..\..\datasets\NER\processed\ner-combined-test.spacy --output ../../datasets/NER/ng2v_5_200_sg-ner.json --gold-preproc



