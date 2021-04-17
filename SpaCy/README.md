this folder does NLP tasks for testing created word embeddings using python nlp SpaCy lib. For training POS and NER tagger and using them to evaluate embeddings.

On the site https://spacy.io/usage/training there is a tool to generate a base_config.cfg file, that you can download. For this the tagger was selected in the tool and for accuracy 
the tagger will only generate tags as token.tag_ which are fine-grained pos.
then that config needs to be filled in with all the other defaults. This generates the config.cfg
python -m spacy init fill-config base_config-pos.cfg config-pos.cfg

if you want to access token.pos_ which is coarse-grained (e.g. NOUN, VERB...), you need to include a morphologizer component in the config under [components]
this is done by creating a template config morfo-config file and copy pasting its morphologizer component into config.cfg under [components] and "morphologizer" under [nlp]
spacy init config -p tagger,morphologizer,parser morfo-config.cfg

For training a model, you need a .spacy format file. To generate it, you use the covert method https://spacy.io/api/cli#convert with options
i converted all 3 (train, dev, test) .conllu files this way from https://github.com/UniversalDependencies/UD_Latvian-LVTB
python -m spacy convert lv_lvtb-ud-test.conllu .\ --converter conllu

i also converted https://github.com/LUMII-AILab/FullStack/tree/master/NamedEntities conll2003 NER files to a single .spacy file for use in training the NER model
python -m spacy convert ..\datasets\NER\data\ .\ --converter ner -n 10

To insert my word embeddings into spaCy, covert them to .spacy format. Embeddings need to be .txt with the first line speficying stats about vectors:
python -m spacy init vectors lv ../../Models/Word2vec_Model/word2vec_5_350_sg.txt ../../Models/Spacy_tagger/word2vec_5_350_vectors --name lv-word2vec-5-350

Then in the config-pos.cfg under [Initialize] set vectors = ^ that path where it output without ""

under [training] set max_epochs = 12 for consistent results. This takes about 2h. Otherwise it says 0 and means unlimited epochs, bet eventually stops training past 100 epochs.

Train the custom model to use in the spaCy nlp pipeline for tagging later.
python -m spacy train config-pos.cfg --output ../../Models/Spacy_tagger/word2vec_5_350_pos --paths.train ./lv_lvtb-ud-train.spacy --paths.dev ./lv_lvtb-ud-dev.spacy

optionally verify config stats are in there like POS tags, embeddings...:
python -m spacy debug data ../../Models/Spacy_tagger/ssg_5_350_pos/model-last/config.cfg

Then run this script to do a POS tag
python nlp_pipe.py