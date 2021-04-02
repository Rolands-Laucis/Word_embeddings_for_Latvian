#this script implements the Gensim python library to create a word embeddings language model from my corpus using Word2Vec Skip-Gram method

#python word2vecModeler.py

from gensim.models import Word2Vec
#from gensim.models.word2vec import LineSentence

corpus_path = "../Cleaned_Corpora/combined_clean_corpus.txt"

print('Starting Skip-Gram training on %s' % corpus_path)
model = Word2Vec(corpus_file=corpus_path, vector_size=200, window=5, workers=2, sg=1)
print('Skip-Gram model done!')

#model = Word2Vec.load("..\Models\Word2vec_model\word2vec.model")

model.save("..\Models\Word2vec_model\word2vec.model")
print('Model saved!')
print('Done!')