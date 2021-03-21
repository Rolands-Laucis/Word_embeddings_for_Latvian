#this script combines any corpus .txt's into 1 text file

#python combineCorpora.py

i = 0
text_paths = [r'..\cleaned_lvwiki.txt', r'..\cleaned_europarl_lv.txt']

done_txt = open(r"..\combined_clean_corpus.txt", "w")
done_txt.write("")
done_txt.close()
print("Cleared file")

done_txt = open(r"..\cleaned_europarl_lv.txt", "a", encoding="utf-8")

print("starting clean")

for path in text_paths:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            i += 1
            done_txt.write(line)
            if i%10000 == 0:
                print("processed %d lines of text" % i)


done_txt.close()
print('done')