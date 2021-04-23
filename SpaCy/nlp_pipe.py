#this script does NLP tasks for testing created word embeddings using python nlp SpaCy lib. For training POS and NER tagger and using them to evaluate embeddings.

#python nlp_pipe.py

import spacy

nlp = spacy.load("../../Models/Spacy_tagger/ssg_5_200_sg_ner/model-best/")

#print(nlp.pipeline)
doc = nlp("\"Šeit ir Latvija,\" sacīja deputāts, akcentējot, ka latviešu valoda \"bija, ir un būs vienīgā valsts valoda\".")

#print("Word | UPOS | TAG")
for token in doc:
    print(token.text, token.ent_type_, token.ent_iob_)
    #print(token.text, token.pos_, token.tag_, token.morph)
