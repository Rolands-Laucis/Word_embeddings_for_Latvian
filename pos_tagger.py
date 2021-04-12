#this script produces a POS tagged text file from a raw input text file using UDPipe lib

#python pos_tagger.py --embeddings_type  --embeddings_file  --input_file  --output_file

from ufal.udpipe import Sentence, Trainer, Model, Pipeline, ProcessingError, InputFormat, OutputFormat, Evaluator

def main():
    #CLI argument handling
    #parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    #parser.add_argument("--embeddings_type", type=str, required=True, help="[word2vec|fasttext_original|fasttext_gensim|ngram2vec|ssg]")
    #parser.add_argument("--embeddings_file", type=str, required=True, help="Path to the .wordvectors, .vec or .txt embeddings file.")
    #parser.add_argument("--input_file", type=str, required=True, help="Path to the raw text file.")
    #parser.add_argument("--output_file", type=str, default=r'../pos_tagging/results.txt', help="Path to the tagged output txt file.")
    #args = parser.parse_args()

    #sentence = Sentence()
    #sentence.setNewDoc(False, "../pos_tagging/UD_Latvian-LVTB-master/lv_lvtb-ud-train.conllu")
    #sentence.setText("../pos_tagging/UD_Latvian-LVTB-master/lv_lvtb-ud-train.conllu")
    #print(sentence.getText())
    #sentences = sentence.setNewDoc(True, "../pos_tagging/UD_Latvian-LVTB-master/lv_lvtb-ud-train.conllu")
    #return

    #input_format = InputFormat.newConlluInputFormat("../pos_tagging/UD_Latvian-LVTB-master/lv_lvtb-ud-train.conllu")

    #trained = udpipe_train("toymodel.udpipe", "../pos_tagging/UD_Latvian-LVTB-master/lv_lvtb-ud-train.conllu", #"file:../pos_tagging/UD_Latvian-LVTB-master/lv_lvtb-ud-train.conllu"
    #            "dimension=24;epochs=10;", 
    #            "iterations=1;provide_xpostag=1;provide_lemma=1;provide_feats=1;", 
    #            "embedding_form_file=../tf-morphotagger-master/embeddings/fasttext_baseline_300.vec")

    #m = Model()

    return
    trained = Trainer.train(Trainer.DEFAULT, Sentence.Sentences , Trainer.DEFAULT, #"file:../pos_tagging/UD_Latvian-LVTB-master/lv_lvtb-ud-train.conllu"
                "dimension=24;epochs=10;", 
                "iterations=1;provide_xpostag=1;provide_lemma=1;provide_feats=1;", 
                "embedding_form_file=../tf-morphotagger-master/embeddings/fasttext_baseline_300.vec")

    print("Done POS tagging!")
    print(trained)

if __name__ == '__main__':
    main()