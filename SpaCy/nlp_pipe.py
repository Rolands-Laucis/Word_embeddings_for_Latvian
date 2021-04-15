#this script does NLP tasks for testing created word embeddings using python nlp SpaCy lib. For training POS and NER tagger and using them to evaluate embeddings.

#On the site https://spacy.io/usage/training there is a tool to generate a base_config.cfg file, that you can download
#then that config needs to be filled in with all the other defaults. This generates the config.cfg
#python -m spacy init fill-config base_config.cfg config.cfg

#For training a model, you need a .spacy format file. To generate it, you use the covert method https://spacy.io/api/cli#convert with options
#i converted all 3 (train, dev, test) .conllu files this way from https://github.com/UniversalDependencies/UD_Latvian-LVTB
#python -m spacy convert lv_lvtb-ud-test.conllu .\ --converter conllu

#To insert my word embeddings into spaCy, covert them to .spacy format:
#python -m spacy init vectors lv ../../Models/SSG_model/ssg_5_200_sg.txt ../../Models/Spacy_tagger/vectors --name lv-ssg-5-200

#Then in the config.cfg under [Initialize] set vectors = ^ that path where it output without ""

#Train the custom model to use in the spaCy nlp pipeline for tagging later.
#python -m spacy train config.cfg --output ../../Models/Spacy_tagger/ssg_5_200_pos --paths.train ./lv_lvtb-ud-train.spacy --paths.dev ./lv_lvtb-ud-dev.spacy

#Then run this script to do a POS tag
#python nlp_pipe.py

#from thinc.api import Config
#from spacy.language import Language
import spacy
from spacy import util
from thinc.api import Config
from spacy.language import Language
from spacy.lang.lv import Latvian
from spacy.vocab import Vocab

#nlp = spacy.load("../../Models/Spacy_tagger/ssg_5_200_pos/model-last/")
config = Config().from_disk("../../Models/Spacy_tagger/ssg_5_200_pos/model-last/config.cfg")
#nlp = Latvian()
#language = spacy.blank("lv")
#nlp = util.load_model_from_config(config)
voc = Vocab(vectors_name="./vocab/vectors")
nlp = Latvian.from_config(config, vocab=voc)
#nlp = language.from_disk("../../Models/Spacy_tagger/ssg_5_200_pos/model-last/")
#nlp.from_disk("../../Models/Spacy_tagger/ssg_5_200_pos/model-last/")

#nlp.initialize(Vocab(vectors_name="./vocab/vectors"))
doc = nlp("astronomija uzbūvi izvietojumu kustību un attīstību.")

print(nlp.pipeline)


#for token in doc:
    #print(token.text, token.pos)
#    print(token.text, token.pos_)
