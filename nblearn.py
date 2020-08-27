import json
import os
import sys
from nltk.corpus import stopwords
import nltk
from nltk.stem import PorterStemmer

# path = '/Users/pooja/Documents/NLP/assignment/train'
path = sys.argv[1]

spam_files = []
ham_files = []
count_ham=0
count_spam=0

word_count_spam = {}
total_spam = 0

word_count_ham = {}
total_ham = 0

vocabulary_size = 0

nltk.download('stopwords')
stop_words = stopwords.words('english')

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' and '.spam' in file:
            count_spam = count_spam + 1
            emailfile = open(os.path.join(r, file), "r", encoding="latin1")
            lines = emailfile.readlines()
            for line in lines:
                for word in line.strip().split(' '):
                    total_spam = total_spam + 1
                    if word.lower() in word_count_spam:
                        word_count_spam[word.lower()] = word_count_spam[word.lower()] + 1
                    else:
                        if word.lower() not in word_count_ham:
                            vocabulary_size = vocabulary_size + 1
                        word_count_spam[word.lower()] = 1
            emailfile.close()
        elif '.txt' and '.ham' in file:
            count_ham = count_ham + 1
            emailfile = open(os.path.join(r, file), "r", encoding="latin1")
            lines = emailfile.readlines()
            for line in lines:
                for word in line.strip().split(' '):
                    total_ham = total_ham + 1
                    if word.lower() in word_count_ham:
                        word_count_ham[word.lower()] = word_count_ham[word.lower()] + 1
                    else:
                        if word.lower() not in word_count_spam:
                            vocabulary_size = vocabulary_size + 1
                        word_count_ham[word.lower()] = 1
            emailfile.close()

for w in word_count_spam:
    # word_count_spam[w] = word_count_spam[w] + 1 /(total_spam + vocabulary_size)
    word_count_spam[w] = (word_count_spam[w] + 1) / float(total_spam + vocabulary_size)
    if w not in word_count_ham:
        word_count_ham[w] = 1 / float(total_ham + vocabulary_size)
for wh in word_count_ham:
    # word_count_ham[wh] = word_count_ham[wh]
    word_count_ham[wh] = (word_count_ham[wh]+1) / float(total_ham + vocabulary_size)
    if wh not in word_count_spam:
        word_count_spam[wh] = 1 / float(total_spam + vocabulary_size)

# word_count_spam_without_stopwords = [word for word in word_count_spam if word not in stop_words]
# word_count_ham_without_stopwords = [word for word in word_count_ham if word not in stop_words]

word_count_spam_without_stopwords = {}
word_count_ham_without_stopwords = {}

# word_count_spam_with_stemming = {}
# word_count_ham_with_stemming = {}

ps = PorterStemmer()

# for w in word_count_spam:
#     word_count_spam_with_stemming[ps.stem(w)] = word_count_spam[w]
#
# for w in word_count_ham:
#     word_count_ham_with_stemming[ps.stem(w)] = word_count_ham[w]

for w in word_count_spam:
    if w not in stop_words:
        word_count_spam_without_stopwords[w] = word_count_spam[w]

for w in word_count_ham:
    if w not in stop_words:
        word_count_ham_without_stopwords[w] = word_count_ham[w]

final_dictionary = {}
total_docs = count_spam + count_ham
pOfSpam = count_spam / float(total_docs)
pOfHam = count_ham / float(total_docs)

print("count spam ", count_spam)
print("count ham ", count_ham)


final_dictionary["spamDictionary"] = word_count_spam_without_stopwords
final_dictionary["hamDictionary"] = word_count_ham_without_stopwords
final_dictionary["POfSpam"] = pOfSpam
final_dictionary["POfHam"] = pOfHam


with open("nbmodel.txt",  "w") as file:
    file.write(json.dumps(final_dictionary))