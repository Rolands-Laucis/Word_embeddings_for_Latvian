@echo off

echo training all NER models
python -m spacy train config-ner.cfg --output ../../Models/Spacy_tagger/ssg_5_200_sg_ner --paths.train ..\..\datasets\NER\processed\ner-combined-train.spacy --paths.dev ..\..\datasets\NER\processed\ner-combined-dev.spacy --paths.vectors C:\Users\Experimenter\Desktop\BD_Code\Models\Spacy_tagger\ssg_5_200_sg_vectors
python -m spacy train config-ner.cfg --output ../../Models/Spacy_tagger/ssg_5_100_sg_ner --paths.train ..\..\datasets\NER\processed\ner-combined-train.spacy --paths.dev ..\..\datasets\NER\processed\ner-combined-dev.spacy --paths.vectors C:\Users\Experimenter\Desktop\BD_Code\Models\Spacy_tagger\ssg_5_100_sg_vectors
python -m spacy train config-ner.cfg --output ../../Models/Spacy_tagger/fasttext_5_200_sg_ner --paths.train ..\..\datasets\NER\processed\ner-combined-train.spacy --paths.dev ..\..\datasets\NER\processed\ner-combined-dev.spacy --paths.vectors C:\Users\Experimenter\Desktop\BD_Code\Models\Spacy_tagger\fasttext_5_200_sg_vectors
python -m spacy train config-ner.cfg --output ../../Models/Spacy_tagger/word2vec_5_200_sg_ner --paths.train ..\..\datasets\NER\processed\ner-combined-train.spacy --paths.dev ..\..\datasets\NER\processed\ner-combined-dev.spacy --paths.vectors C:\Users\Experimenter\Desktop\BD_Code\Models\Spacy_tagger\word2vec_5_200_sg_vectors
python -m spacy train config-ner.cfg --output ../../Models/Spacy_tagger/ng2v_5_200_sg_ner --paths.train ..\..\datasets\NER\processed\ner-combined-train.spacy --paths.dev ..\..\datasets\NER\processed\ner-combined-dev.spacy --paths.vectors C:\Users\Experimenter\Desktop\BD_Code\Models\Spacy_tagger\ng2v_5_200_sg_vectors

echo evaluating all NER models
python -m spacy evaluate ..\..\Models\Spacy_tagger\ssg_5_200_sg_ner\model-best ..\..\datasets\NER\processed\NER_concatinated-test.spacy --output ../../datasets/NER/ssg_5_200_sg_ner.json --gold-preproc
python -m spacy evaluate ..\..\Models\Spacy_tagger\ssg_5_100_sg_ner\model-best ..\..\datasets\NER\processed\NER_concatinated-test.spacy --output ../../datasets/NER/ssg_5_100_sg_ner.json --gold-preproc
python -m spacy evaluate ..\..\Models\Spacy_tagger\fasttext_5_200_sg_ner\model-best ..\..\datasets\NER\processed\NER_concatinated-test.spacy --output ../../datasets/NER/fasttext_5_200_sg_ner.json --gold-preproc
python -m spacy evaluate ..\..\Models\Spacy_tagger\word2vec_5_200_sg_ner\model-best ..\..\datasets\NER\processed\NER_concatinated-test.spacy --output ../../datasets/NER/word2vec_5_200_sg_ner.json --gold-preproc
python -m spacy evaluate ..\..\Models\Spacy_tagger\ng2v_5_200_sg_ner\model-best ..\..\datasets\NER\processed\NER_concatinated-test.spacy --output ../../datasets/NER/ng2v_5_200_sg_ner.json --gold-preproc