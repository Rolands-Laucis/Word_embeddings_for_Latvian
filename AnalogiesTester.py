#This script tests generated word embedding model (word vector space) accuracy on a Latvian analogy data set

#python AnalogiesTester.py --model_type word2vec --model_file ../Models/Word2vec_model/word2vec.wordvectors --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_word2vec_3cosmul.txt --gen_output true --eval_method 3cosmul --topn 10 --verbose true
#python AnalogiesTester.py --model_type fasttext --model_file ../Models/FastText_model/FastText_combined_corp_model.wordvectors --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_fasttext.txt --gen_output true
#python AnalogiesTester.py --model_type ssg --model_file ../Models/SSG_model/ssg_model.txt --dataset_file ../datasets/lv-analogies.txt --output_file ../datasets/results_ssg.txt --gen_output true

import argparse
from gensim.models import Word2Vec, KeyedVectors, fasttext

def main():
    #CLI argument handling
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--model_type", type=str, required=True, help="[word2vec|fasttext|ngram2vec|ssg]")
    parser.add_argument("--model_file", type=str, required=True, help="Path to the .wordvectors or .txt file.")
    parser.add_argument("--dataset_file", type=str, required=True, help="Path to the dataset txt file.")
    parser.add_argument("--eval_method", type=str, required=True, help="[gensim|3cosmul|3cosadd]")
    parser.add_argument("--topn", type=int, default=1, help="Answer accepted, if in topn results from similarity check. Default 1.")
    parser.add_argument("--dummy4unknown", type=bool, default=True, help="Should the analogy line be skipped, if not all words in vocabulary? Default True.")
    parser.add_argument("--verbose", type=bool, default=False, help="Should the program give status updates? Default False.")
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
    #word_vectors = KeyedVectors.load_word2vec_format(args.model_file,binary=False, encoding='utf8')
    #word_vectors = model.wv
    #del model
    #word_vectors.save("../Models/FastText_model/fasttext_oficial_lv_300.wordvectors")
    #return
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

    #evaluate the model by different methods
    score = 0
    sections = None

    if args.eval_method == "gensim":
        score, sections = word_vectors.evaluate_word_analogies(args.dataset_file, case_insensitive=True, dummy4unknown=args.dummy4unknown)
    elif args.eval_method == "3cosmul" or args.eval_method == "3cosadd":
        score, sections = AnalogyEval(args.dataset_file, word_vectors, args.eval_method, args.topn, args.dummy4unknown)
    else:
        print("eval_method not supported!")
        return

    
    #output evaluation results
    if args.gen_output:
        output = open(args.output_file, "a", encoding='utf-8')
        output.write("%1.6f,%s,%s,%d,%r\n" % (score*100, args.model_type, args.eval_method, args.topn, args.dummy4unknown))
        #output.write("Dataset evaluated with score: %1.6f%% and parameters %s %s %d %r \n incorrect guesses: \n" % (score*100, args.model_type, args.eval_method, args.topn, args.dummy4unknown))

        if False:
            if args.eval_method == "gensim":
                for section in sections:
                    for line in section['incorrect']:
                        for word in line:
                            output.write("%s " % word)
                        output.write('\n')
            elif args.eval_method == "3cosmul" or args.eval_method == "3cosadd":
                for line in sections['incorrect']:
                        for word in line:
                            output.write("%s " % word)
                        #print(line)
                        output.write('\n')
        output.close()
    
    print("Dataset evaluated with score: %1.6f" % score)
    #print("Dataset evaluated!")


#evaluates a analogy dataset .txt file and returns a score (0-1) of how many were answered correctly
def AnalogyEval(file, word_vectors, method, top, dummy4unknown):
    words_proccessed = 0
    correct_answers = []
    incorrect_answers = []

    #go through analogies file line by line and check the 4 word analogy evaluation
    with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                words = lowercaseWords(line.split()) #get all 4 words from line
                if (":" in words) or (len(words) != 4): #if this line describes a new category, not 4 words of analogies
                    continue

                #check if all required words are in vocabulary - dummy4unknown
                if dummy4unknown:
                    skip_line = False
                    for n in range(0,3):
                        #try:
                        #    word_vectors.get_vector(words[n])
                        #except:
                        #    skip_line = True
                        #    break
                        if word_vectors.has_index_for(words[n]) == False:
                            skip_line = True
                            break
                    if skip_line:
                        continue
                
                #get answer or answers
                answer = None

                if method == "3cosmul":
                    answer = word_vectors.most_similar_cosmul(positive=[words[1],words[2]], negative=[words[0]], topn=top)
                elif method == "3cosadd":
                    answer = word_vectors.most_similar(positive=[words[1],words[2]], negative=[words[0]], topn=top)
                
                #count score
                if words[3] in dict(answer):
                    correct_answers.append(words)
                else:
                    incorrect_answers.append(words)
                words_proccessed += 1

                #status update and/or break condition
                if words_proccessed%100 == 0:
                    print("processed %d lines of analogies" % words_proccessed)
                    #print(words)
                    #print(dict(answer))
                    #break
    return (len(correct_answers)/words_proccessed), {"correct":correct_answers, "incorrect":incorrect_answers}

def lowercaseWords(words):
    w = []
    for word in words:
        w.append(word.lower())
    return w

if __name__ == '__main__':
    main()