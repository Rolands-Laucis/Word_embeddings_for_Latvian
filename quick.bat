@echo off

echo training ssg lemmatized...
cd ..\wang2vec-master
echo 5 200 lem
word2vec -train ../Cleaned_Corpora/combined_clean_corpus_lem.txt -output ../Models/SSG_model/ssg_5_200_sg_lem.txt -type 3 -size 200 -window 5 -binary 0
echo 5 300 lem
word2vec -train ../Cleaned_Corpora/combined_clean_corpus_lem.txt -output ../Models/SSG_model/ssg_5_300_sg_lem.txt -type 3 -size 300 -window 5 -binary 0