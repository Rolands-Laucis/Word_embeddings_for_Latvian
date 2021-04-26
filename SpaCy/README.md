##This folder does NLP tasks for testing created word embeddings using python nlp SpaCy lib. For training POS and NER tagger and using them to evaluate embeddings.
These commands contain relative paths from inside this folder, so run them from this dir.

#On the site https://spacy.io/usage/training there is a tool to generate a base_config.cfg file, that you can download. For this the tagger was selected in the tool and for accuracy 
#the tagger will only generate tags as token.tag_ which are fine-grained pos.
#then that config needs to be filled in with all the other defaults. This generates the config.cfg
python -m spacy init fill-config base_config-ner.cfg config-ner.cfg

#if you want to access token.pos_ which is coarse-grained (e.g. NOUN, VERB...), you need to include a morphologizer component in the config under [components]
#this is done by creating a template config morfo-config file and copy pasting its morphologizer component into config.cfg under [components] and "morphologizer" under [nlp]
spacy init config -p tagger,morphologizer,parser morfo-config.cfg

#For training a model, you need a .spacy format file. To generate it, you use the covert method https://spacy.io/api/cli#convert with options
#I converted all 3 (train, dev, test) .conllu files this way from https://github.com/UniversalDependencies/UD_Latvian-LVTB
python -m spacy convert lv_lvtb-ud-test.conllu .\ --converter conllu

#I found 2 NER datasets for Latvian. 
#https://github.com/LUMII-AILab/FullStack/tree/master/NamedEntities of nonstandard .conll2003 format which i call LUMII NER and 
#https://github.com/accurat-toolkit/TildeNER/tree/master/TEST of .gold format which i call TildeNER in these files.
#Neither are acepted by spaCy converter, so i had to convert them myself. I chose .iob format, because it had the simplest format and i had tested, that spaCy was okay with it.
#I concatinate both sets and prepare a single large .iob file from both sets, that just includes the fields token and NER tag, which spaCy cares about.
#Optionaly you can include token, POS and NER tag fields, but LUMII has normal format UPOS tags and TildeNER has some weird 1 char long i guess POS tags. SpaCy doesnt like that.
#Settings and file locations are set manually in script. It produces a bunch of files through its processing stages, but the end we care about is the 3 .iob files (train, dev, test)
#which are split by sentence count in % ratios of 60-30-10
cd ..
cd misc
python ner_file_concat.py

#To make a .spacy file for use in training the NER model.
python -m spacy convert ..\..\datasets\NER\processed\ner-combined-train.iob ..\..\datasets\NER\processed\ -l lv
python -m spacy convert ..\..\datasets\NER\processed\ner-combined-dev.iob ..\..\datasets\NER\processed\ -l lv
python -m spacy convert ..\..\datasets\NER\processed\ner-combined-test.iob ..\..\datasets\NER\processed\ -l lv

#To insert my word embeddings into spaCy, covert them to .spacy format. Embeddings need to be .txt (so it says in docs, but i found extension doesnt matter) with the first line speficying stats about vectors:
python -m spacy init vectors lv ../../Models/SSG_model/ssg_5_100_sg.txt ../../Models/Spacy_tagger/ssg_5_100_sg_vectors --name lv-ssg-5-100
python -m spacy init vectors lv ..\\..\ngram2vec-master\outputs\combined_clean_corpus\ngram_ngram\sgns\ng2v_5_200_sg.output ../../Models/Spacy_tagger/ng2v_5_200_sg_vectors --name lv-ng2v-5-200

#Then in the config-pos.cfg under [Initialize] set vectors = ^ that path where it output without "" OR add a CLI argument --paths.vectors with path to the created vectors folder

#under [training] set max_epochs = 12 for consistent results. This takes about 3h. Otherwise it says 0 and means unlimited epochs, bet eventually stops training past 100 epochs.

##Train the custom model to use in the spaCy nlp pipeline for tagging later.
python -m spacy train config-pos.cfg --output ../../Models/Spacy_tagger/ng2v_5_200_sg_pos --paths.train ./lv_lvtb-ud-train.spacy --paths.dev ./lv_lvtb-ud-dev.spacy
python -m spacy train config-ner.cfg --output ../../Models/Spacy_tagger/ssg_5_200_sg_ner --paths.train ..\..\datasets\NER\processed\ner-combined-train.spacy --paths.dev ..\..\datasets\NER\processed\ner-combined-dev.spacy

#optionally verify config stats are in there like POS tags, embeddings...:
python -m spacy debug data ../../Models/Spacy_tagger/ssg_5_350_pos/model-last/config.cfg

##Then run this script to work with the pipeline, i.e. get tags and pos and any info about a sentence or documents programmatically:
python nlp_pipe.py

#Or use spaCy evaluate CLI command on the test data https://spacy.io/api/cli#evaluate:
python -m spacy evaluate ..\\..\Models\Spacy_tagger\ng2v_5_200_sg_pos\model-best ./lv_lvtb-ud-test.spacy --output ../../datasets/POS/ng2v_5_200_sg_pos.json --gold-preproc
python -m spacy evaluate ..\..\Models\Spacy_tagger\word2vec_5_200_sg-ner\model-best ..\..\datasets\NER\processed\ner-combined-test.spacy --output ../../datasets/NER/word2vec_5_200_sg-ner.json --gold-preproc

#Debug spaCy config, if results are weird or some other issues:
python -m spacy debug data ./config-ner.cfg --paths.train ..\..\datasets\NER\processed\ner-combined-train.spacy --paths.dev ..\..\datasets\NER\processed\ner-combined-dev.spacy --paths.vectors C:\Users\Experimenter\Desktop\BD_Code\Models\Spacy_tagger\ssg_5_200_sg_vectors -V