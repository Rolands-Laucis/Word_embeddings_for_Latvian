#this script implements the fastText python library to create a word embeddings language model from my corpus

#python FastTextModeler.py

import fasttext

model = None

def Train(model_type):
    model = fasttext.train_unsupervised('../cleaned_lvwiki.txt', model=model_type)
    model.save_model("../FastText_lvwiki_model.bin")

def WorkWithModel(model_name):
    model = fasttext.load_model(model_name)
    while True:
        txt = input("ievadi vardu: ")
        print(model.get_nearest_neighbors(txt))

Train('skipgram')
#WorkWithModel('../FastText_lvwiki_model.bin')


print ("Done!")