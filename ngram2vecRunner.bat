::./ngram2vecRunner.bat

cd ..\Ngram2Vec_repo\ngram2vec-master\ngram2vec

::python pairs2vocab.py -h

::python corpus2vocab.py --corpus_file ..\..\..\Cleaned_Corpora\combined_clean_corpus.txt --vocab_file ..\..\..\Models\Ngram2vec_model\vocab --feature ngram --order 2

python corpus2pairs.py --corpus_file ..\..\..\Cleaned_Corpora\combined_clean_corpus.txt --pairs_file ..\..\..\Models\Ngram2vec_model\pairs --vocab_file ..\..\..\Models\Ngram2vec_model\vocab --cooccur ngram_ngram

::change dir to my python script
cd ..\..\..\BD_Word_Embeddings

:: concatinate all pairs files into 1 file
python ngram2vec_pairs_concat.py

::change dir back
cd ..\Ngram2Vec_repo\ngram2vec-master\ngram2vec

::python pairs2vocab.py --pairs_file ..\..\..\Models\Ngram2vec_model\pairs.txt --input_vocab_file ..\..\..\Models\Ngram2vec_model\vocab.input --output_vocab_file ..\..\..\Models\Ngram2vec_model\vocab.output

::python pairs2sgns.py --pairs_file ..\..\..\Models\Ngram2vec_model\pairs --input_vocab_file ..\..\..\Models\Ngram2vec_model\vocab.input --output_vocab_file ..\..\..\Models\Ngram2vec_model\vocab.output --output_vector_file ..\..\..\Models\Ngram2vec_model\sgns.output --input_vector_file ..\..\..\Models\Ngram2vec_model\sgns.input --size 200 --threads_num 2

cd ..\word2vec
word2vec.exe --pairs_file ..\..\..\Models\Ngram2vec_model\pairs.txt --input_vocab_file ..\..\..\Models\Ngram2vec_model\vocab.input --output_vocab_file ..\..\..\Models\Ngram2vec_model\vocab.output --output_vector_file ..\..\..\Models\Ngram2vec_model\sgns.output --input_vector_file ..\..\..\Models\Ngram2vec_model\sgns.input --size 200 --threads_num 2