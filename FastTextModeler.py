#this script implements the fastText python library to create a word embeddings language model from my corpus using FastText method with gensim.

#python FastTextModeler.py

from gensim.models import FastText
#import fasttext
corpus_file = r"../Cleaned_Corpora/combined_clean_corpus.txt"

model = FastText(vector_size=4, window=3, min_count=1)
model.build_vocab(corpus_file=corpus_file)
print("Built vocab. Starting train...")

#train
model.train(corpus_file=corpus_file, total_words=model.corpus_total_words, epochs=5)

model.wv.save(r'../Models/FastText_model/FastText_combined_corp_model.wordvectors')
#def Train(model_type):
#    model = fasttext.train_unsupervised('../cleaned_lvwiki.txt', model=model_type)
#    model.save_model("../FastText_lvwiki_model.bin")

#def WorkWithModel(model_name):
#    model = fasttext.load_model(model_name)
#    while True:
#        txt = input("ievadi vardu: ")
#        print(model.get_nearest_neighbors(txt))

#Train('skipgram')
#WorkWithModel('../FastText_lvwiki_model.bin')


print ("Done!")