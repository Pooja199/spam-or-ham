import json
import os
import math
import sys
import random
from nltk.stem import PorterStemmer

trained_data = json.loads(open("nbmodel.txt", "r").read())
path = sys.argv[1]

trained_spam_dictionary = trained_data["spamDictionary"]
trained_ham_dictionary = trained_data["hamDictionary"]

dev_files = []

for r, d, f in os.walk(path):
    for file in f:
        if ".txt" in file:
            dev_files.append(os.path.join(r, file))
        # print (os.path.basename(path) + "/" + os.path.join(r, file).strip(path))


#TODO check if this is 0


choice_list = ["spam", "ham"]
ps = PorterStemmer()

fout = open("nboutput.txt", "w")
for r, d, f in os.walk(path):
    for file in f:
        probability_of_spam_given_msg = math.log2(trained_data["POfSpam"])
        probability_of_ham_given_msg = math.log2(trained_data["POfHam"])
        if ".txt" in file:
            emailfile = open(os.path.join(r, file), "r", encoding="latin1")
            lines = emailfile.read()
            words = lines.split()
            for word in words:
                # word = ps.stem(word)
                if word.lower() in trained_spam_dictionary:
                    probability_of_spam_given_msg = probability_of_spam_given_msg + math.log2(trained_spam_dictionary[word.lower()])
                if word.lower() in trained_ham_dictionary:
                    probability_of_ham_given_msg = probability_of_ham_given_msg + math.log2(trained_ham_dictionary[word.lower()])
            if probability_of_spam_given_msg > probability_of_ham_given_msg:
                fout.write("spam" + "\t" + os.path.join(r, file) + "\n")
            elif probability_of_ham_given_msg > probability_of_spam_given_msg:
                fout.write("ham" + "\t" + os.path.join(r, file) + "\n")
            else:
                if probability_of_ham_given_msg == probability_of_spam_given_msg:
                    random.choice(choice_list)
fout.close()