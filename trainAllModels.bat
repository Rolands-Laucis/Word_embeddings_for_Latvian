@echo off

echo training fasttext...
python FastTextModeler.py --corpus_file ../Cleaned_Corpora/combined_clean_corpus.txt --window 5 --vector_size 200 --method sg

echo training word2vec...
python word2vecModeler.py --corpus_file ../Cleaned_Corpora/combined_clean_corpus.txt --window 5 --vector_size 200 --method sg

echo training ngram2vec...
echo ngram2vec not supported

echo training ssg...
cd ..\wang2vec_repo\wang2vec-master && bash && 
./word2vec -train ../../Cleaned_Corpora/combined_clean_corpus.txt -output ../../Models/SSG_model/vec.txt -type 3 -size 200 -window 5 -binary 0

echo done training models