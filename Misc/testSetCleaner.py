#this script quickly cleans a small corpus sample with the given regex rules, as a quick test to check the cleaning rules

#python testSetCleaner.py

import re
from regex_rules import *

done_txt = open(r"..\..\test_corpus_DONE.txt", "w", encoding="utf-8")
done_txt.write("")
done_txt.close()
print("Cleared file")

done_txt = open(r"..\..\test_corpus_DONE.txt", "a", encoding="utf-8")

with open(r"..\..\corpus_test.txt", "r", encoding="utf-8") as f:
    for line in f:
        #gets rid of uppercase abreviations
        line = re.sub('([A-ZĀČĒĢĪĶĻŅŠŪŽ]{2})+', '', line)
        
        line = line.lower()
        for old, new in RE_replacements_new:
            line = re.sub(old, new, line)
        #line = re.sub(r'[-\[\]\(\)=]', ' ', line).sub(r'\d*', '0', line).sub(r'\s*', ' ', line)
        #print(line)
        done_txt.write(line)

done_txt.close()
print('done')