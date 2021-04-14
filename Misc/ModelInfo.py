#this script is used to get meta info about a trained word embedding model

#python ModelInfo.py

import fasttext
import re

corpora = ['../corpus_test.txt']
models = [('fasttext', '../FastText_lvwiki_model.bin')]

def GetWordCountOfModels(m):
    for model in m:
        if model[0] == 'fasttext':
            current_model = fasttext.load_model(model[1])
            print("%s model word count: %d" % (model[1], len(current_model.words)))
        else:
            pass

def GetWordCountOfCorpora(c):
    for corpus in c:
        wordCount = 0
        with open(corpus, 'r', encoding="utf-8") as f:
            for line in f:
                words = line.split()
                for word in words:
                    if re.match(r'\(?[aābcčdeēfgģhiījkķlļmnņoprsštuūvzž]+\)?', word, flags=re.IGNORECASE):
                        wordCount += 1
        print("Word count in corpus %s is %d" % (corpus, wordCount))


#GetWordCountOfModels(models)
GetWordCountOfCorpora(corpora)