#ModelTypeTransform.py --input_file_type wordvectors --input_file ..\Models\Word2vec_model\word2vec_5_200_sg.wordvectors --output_file_type bin --output_file ..\Models\Word2vec_model\word2vec_5_200_sg.bin

import argparse
from gensim.models import Word2Vec,fasttext

def main():
    #CLI arguments
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--input_file_type", type=str, required=True, help="[bin|txt|wordvectors|vec|model]")
    parser.add_argument("--input_file", type=str, default='', help="Path to the input file including extention.")
    parser.add_argument("--output_file_type", type=str, required=True, help="[bin|txt|wordvectors]")
    parser.add_argument("--output_file", type=str, default='', help="Path to the output file including extention.")
    args = parser.parse_args()

    word_vectors = None

    #load model of file type
    if args.input_file_type == "bin":
        word_vectors = KeyedVectors.load_word2vec_format(args.input_file, binary=True)
    elif args.input_file_type == "txt":
        word_vectors = KeyedVectors.load_word2vec_format(args.input_file, binary=False)
    elif args.input_file_type == "wordvectors":
        word_vectors = KeyedVectors.load(args.input_file, mmap='r')
    elif args.input_file_type == "vec":
        word_vectors = fasttext.load_facebook_vectors(args.input_file)
    elif args.input_file_type == "model":
        word_vectors = Word2Vec.load(args.input_file).wv
    else:
        print("input_file_type not supported!")
        return
    print("model loaded!")

    #save model of file type
    if args.output_file_type == "bin":
        word_vectors.save_word2vec_format(args.output_file, binary=True)
    elif args.output_file_type == "txt":
        word_vectors.save_word2vec_format(args.output_file, binary=False)
    elif args.output_file_type == "wordvectors":
        word_vectors.save(args.output_file)
    else:
        print("output_file_type not supported!")
        return
    print("model saved!")

if __name__ == '__main__':
    main()