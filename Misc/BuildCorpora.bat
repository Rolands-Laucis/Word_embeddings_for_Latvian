@echo off
cd ..

echo preproccessing and creating text corpora
python wikiCleaner.py
python europarlCorpus.py
python combineCorpora.py
pause