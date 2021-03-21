import re
from regex_rules import *

done_txt = open(r".\test_corpus_DONE.txt", "w", encoding="utf-8")
done_txt.write("")
done_txt.close()
print("Cleared file")

done_txt = open(r".\test_corpus_DONE.txt", "a", encoding="utf-8")

with open(r".\test_corpus.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.lower()
        for old, new in RE_replacements:
            line = re.sub(old, new, line)
        #line = re.sub(r'[-\[\]\(\)=]', ' ', line).sub(r'\d*', '0', line).sub(r'\s*', ' ', line)
        #print(line)
        done_txt.write(line)

done_txt.close()
print('done')