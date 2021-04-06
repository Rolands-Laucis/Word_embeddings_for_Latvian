#This script tests generated word embedding model (word vector space) accuracy on a Latvian analogy data set

#python AnalogiesTester.py --model_type word2vec --model_file ../Models/Word2vec_model/word2vec.wordvectors --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_word2vec.txt --gen_output true
#python AnalogiesTester.py --model_type fasttext --model_file ../Models/FastText_model/FastText_combined_corp_model.wordvectors --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_fasttext.txt --gen_output true
#python AnalogiesTester.py --model_type ssg --model_file ../Models/SSG_model/ssg_model.txt --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_ssg.txt --gen_output true

import argparse
from gensim.models import Word2Vec, KeyedVectors, fasttext

def main():
    #CLI argument handling
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--model_type", type=str, required=True, help="[word2vec|fasttext|ngram2vec|ssg]")
    parser.add_argument("--model_file", type=str, required=True, help="Path to the .wordvectors file.")
    parser.add_argument("--dataset_file", type=str, required=True, help="Path to the dataset txt file.")
    parser.add_argument("--gen_output", type=bool, default=False, help="Should the output file with score and incorrect guesses be generated. Default False.")
    parser.add_argument("--output_file", type=str, default=r'../datasets/results.txt', help="Path to the output txt file.")
    args = parser.parse_args()

    if args.gen_output:
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
    if args.model_type == "word2vec":
        word_vectors = KeyedVectors.load(args.model_file, mmap='r')
    elif args.model_type == "fasttext":
        #supposed to load the fasttext lib generated .bin file, but not enough ram
        #word_vectors = fasttext.load_facebook_vectors(args.model_file)
        
        #this loads gensim FastText generated .wordvectors file
        word_vectors = KeyedVectors.load(args.model_file, mmap='r')
    elif args.model_type == "ssg":
        word_vectors = KeyedVectors.load_word2vec_format(args.model_file, binary=False)
    else:
        print("model_type not supported!")
        return
    print("model loaded!")

    #open dataset file and go through line by line
    score, sections = word_vectors.evaluate_word_analogies(args.dataset_file, case_insensitive=True)
    if args.gen_output:
        output.write("Dataset evaluated with score: %1.6f. incorrect guesses: \n" % score)
        for section in sections:
            for line in section['incorrect']:
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
    #print("Dataset evaluated!")

if __name__ == '__main__':
    main()