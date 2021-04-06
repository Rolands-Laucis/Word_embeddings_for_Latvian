#This script tests generated word embedding model (word vector space) accuracy on a Latvian analogy data set

#python AnalogiesTester.py --model_file ../Models/Word2vec_model/word2vec.wordvectors --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results.txt

import argparse
from gensim.models import Word2Vec, KeyedVectors

def main():
    #CLI argument handling
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--model_file", type=str, required=True, help="Path to the .wordvectors file.")
    parser.add_argument("--dataset_file", type=str, required=True, help="Path to the dataset txt file.")
    parser.add_argument("--output_file", type=str, required=True, help="Path to the output txt file.")
    args = parser.parse_args()

    #clear output file for new output data
    output = open(args.output_file, "w", encoding='utf-8')
    output.write("")
    output.close()
    print("Cleared dataset output file")
    output = open(args.output_file, "a", encoding='utf-8')

    #model loading
    #model = Word2Vec.load(args.model_file)
    #word_vectors = model.wv
    #del model
    #word_vectors.save("../Models/Word2vec_model/word2vec.wordvectors")
    word_vectors = KeyedVectors.load(args.model_file, mmap='r')
    print("model loaded!")

    #open dataset file and go through line by line
    score, sections = word_vectors.evaluate_word_analogies(args.dataset_file, case_insensitive=True)
    output.write("Dataset evaluated with score: %1.6f. correct guesses: \n" % score)
    for section in sections:
        for line in section['correct']:
            for word in line:
                output.write("%s " % word)
            output.write('\n')
    print("Dataset evaluated with score: %1.6f" % score)
    #print(sections)

    #with open(args.dataset_file, 'r', encoding='utf-8') as f:
     #   i = 0
      #  for line in f:
       #     if i == 0:
        #        pass
         #   i += 1
          #  words = line.split() #get all 4 words from line
           # print(words)


            #if i%10 == 0:
             #   print("processed %d lines of text" % i)
              #  break;
            
    
    output.close()
    print("Dataset evaluated!")

if __name__ == '__main__':
    main()