#this script is used to get meta info about a trained word embedding model

#python ModelInfo.py

import fasttext

models = [('fasttext', '../FastText_lvwiki_model.bin')]

def GetWordCountOf(m):
    for model in m:
        if model[0] == 'fasttext':
            current_model = fasttext.load_model(model[1])
            print("%s model word count: %d" % (model[1], len(current_model.words)))
        else:
            pass

GetWordCountOf(models)