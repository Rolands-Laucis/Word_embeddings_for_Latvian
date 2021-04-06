file_path = r'../Models/Ngram2vec_model/'
files = [r'pairs_0', r'pairs_1', r'pairs_2', r'pairs_3']

output_file = open(file_path + r"pairs.txt", "w", encoding="utf-8")
output_file.write("")
output_file.close()
print("Cleared concatenated output pairs text file")

output_file = open(file_path + r"pairs.txt", "a", encoding="utf-8")

for pairs_file in files:
    with open(file_path+pairs_file, 'r', encoding='utf-8') as f:
        for line in f:
            output_file.write(line)
        print('%s appended...' % pairs_file)


output_file.close()
print('Done! Concatinated ngram2vec pairs files.')