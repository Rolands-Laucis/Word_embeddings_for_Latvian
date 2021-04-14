::trainAllModels.bat 5 200
@echo off

::set up arguments
set win=%1
set v_size=%2

::echo training fasttext...
::python FastTextModeler.py --corpus_file ../Cleaned_Corpora/combined_clean_corpus.txt --window %win% --vector_size %v_size% --method sg --output_file ..\Models\FastText_model\fasttext_%win%_%v_size%_sg.wordvectors
echo training fasttext lemmatized...
python FastTextModeler.py --corpus_file ../Cleaned_Corpora/combined_clean_corpus_lem.txt --window %win% --vector_size %v_size% --method sg --output_file ..\Models\FastText_model\fasttext_%win%_%v_size%_sg_lem.wordvectors

::echo training word2vec...
::python word2vecModeler.py --corpus_file ../Cleaned_Corpora/combined_clean_corpus.txt --window %win% --vector_size %v_size% --method sg --output_file ..\Models\Word2vec_model\word2vec_%win%_%v_size%_sg.wordvectors
echo training word2vec lemmatized...
python word2vecModeler.py --corpus_file ../Cleaned_Corpora/combined_clean_corpus_lem.txt --window %win% --vector_size %v_size% --method sg --output_file ..\Models\Word2vec_model\word2vec_%win%_%v_size%_sg_lem.wordvectors

echo training ssg...
cd ..\wang2vec-master 
::word2vec -train ../Cleaned_Corpora/combined_clean_corpus.txt -output ../Models/SSG_model/ssg_%win%_%v_size%_sg.txt -type 3 -size %v_size% -window %win% -binary 0
::echo training ssg lemmatized...
::word2vec -train ../Cleaned_Corpora/combined_clean_corpus_lem.txt -output ../Models/SSG_model/ssg_%win%_%v_size%_sg_lem.txt -type 3 -size %v_size% -window %win% -binary 0

echo training ngram2vec...
echo ngram2vec should be done seperately
::cd ..\ngram2vec-master
::bash
::ngram_example.sh %win% %v_size%

echo done training models