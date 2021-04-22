#this script does NLP tasks for testing created word embeddings using python nlp SpaCy lib. For training POS and NER tagger and using them to evaluate embeddings.

#python nlp_pipe.py

import spacy

nlp = spacy.load("../../Models/Spacy_tagger/fasttext_5_200_pos/model-best/")

#print(nlp.pipeline)
doc = nlp("astronomija uzbūvi izvietojumu kustību un attīstību.")

#print("Word | UPOS | TAG")
for token in doc:
    #print(token.text, token.pos)
    print(token.text, token.pos_, token.tag_, token.morph)
