python -m spacy init vectors lv C:\Users\Experimenter\Desktop\BD_Code\ngram2vec-master\outputs\combined_clean_corpus\ngram_ngram\sgns\ng2v_5_200_sg.output ../../Models/Spacy_tagger/ng2v_5_200_sg_vectors --name lv-ng2v-5-200

python -m spacy train ./configs/config-pos.cfg --output ../../Models/Spacy_tagger/ng2v_5_200_sg-pos --paths.train --paths.train ./lvtb-pos-spacy/lv_lvtb-ud-train.spacy --paths.dev ./lvtb-pos-spacy/lv_lvtb-ud-dev.spacy --paths.vectors ..\..\Models\Spacy_tagger\ng2v_5_200_sg_vectors
python -m spacy evaluate ..\..\Models\Spacy_tagger\ng2v_5_200_sg-pos\model-best ./lvtb-pos-spacy/lv_lvtb-ud-test.spacy --output ../../datasets/POS/ng2v_5_200_sg-pos.json --gold-preproc

python -m spacy train ./configs/config-ner.cfg --output ../../Models/Spacy_tagger/ng2v_5_200_sg-ner --paths.train ./lumii-ner-spacy/ner-combined-train.spacy --paths.dev ./lumii-ner-spacy/ner-combined-dev.spacy --paths.vectors ..\..\Models\Spacy_tagger\ng2v_5_200_sg_vectors
python -m spacy evaluate ..\..\Models\Spacy_tagger\ng2v_5_200_sg-ner\model-best ./lumii-ner-spacy/ner-combined-test.spacy --output ../../datasets/NER/ng2v_5_200_sg-ner.json --gold-preproc