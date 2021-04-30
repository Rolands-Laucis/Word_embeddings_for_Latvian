@echo off

::./quick.bat

echo doing quick

python -m spacy init vectors lv ../../Models/FastText_model/fasttext_baseline_300.vec ../../Models/Spacy_tagger/fasttext_baseline_vectors --name lv-ft-bsl

python -m spacy convert ..\..\datasets\POS\tagged_lv_conllu\lv_lvtb-ud-train.conllu .\ -l lv

python -m spacy train config-pos.cfg --output ../../Models/Spacy_tagger/fasttext_baseline_300-pos --paths.train .\lv_lvtb-ud-train.spacy --paths.dev .\lv_lvtb-ud-dev.spacy --paths.vectors ..\..\Models\Spacy_tagger\fasttext_baseline_vectors

python -m spacy evaluate ..\..\Models\Spacy_tagger\fasttext_baseline_300-pos\model-best ./lv_lvtb-ud-test.spacy --output ../../datasets/POS/fasttext_baseline_300-pos.json --gold-preproc
