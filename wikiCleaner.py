#this script cleans the lavian wikipedia data dump .xml file to a clean text file given my regex rules

#python wikiCleaner.py

from wiki_dump_reader import Cleaner, iterate
import re
from regex_rules import *
#import importlib
#import os
#path_to_lvwiki = os.path.join('C:', os.sep, 'meshes', 'as')

#importlib.import_module('regex_rules')

i = 0
cleaned_text_string = ""

f = open(r"..\cleaned_lvwiki.txt", "w")
f.write("")
f.close()
print("Cleared file")

f = open(r"..\cleaned_lvwiki.txt", "a", encoding="utf-8")

print("starting clean")

cleaner = Cleaner()

for title, text in iterate(r"..\lvwiki-latest-pages-articles.xml"):
    text = cleaner.clean_text(text)
    cleaned_text, _ = cleaner.build_links(text)
    cleaned_text_string += cleaned_text
    i += 1
    if i%1000 == 0:
        #lowercase the string
        cleaned_text_string = cleaned_text_string.lower()

        #perform all regex checks on it
        for old, new in RE_replacements: #RE_replacements_simple works pretty much the same speed
            cleaned_text_string = re.sub(old, new, cleaned_text_string)

        #write it to file and reset
        f.write(cleaned_text_string)
        cleaned_text_string = ""
        #print(cleaned_text)
        print("Gone through %d iterations and appended to file" % i)
        #if i >= 10000:
        #    break
    

f.close()

print("cleaned and saved in file!")