f = open("nboutput.txt")
lines = f.readlines()

actual_spam = 0
actual_ham =0
predicted_spam = 0
predicted_ham = 0
correctly_classified_documents = 0
total_documents = 0
correctly_classified_as_spam = 0
correctly_classified_as_ham = 0
actual_file = ""
count =0
for line in lines:
    if ".txt" in line:
        count = count +1

print ("count ", count)

for line in lines:
    if ".spam.txt" in line:
        actual_spam = actual_spam + 1
        actual_file = "spam"
    elif ".ham.txt" in line:
        actual_file = "ham"
        actual_ham = actual_ham + 1
    if line[:3]=="ham":
        label = "ham"
        predicted_ham = predicted_ham + 1
    elif line[:4]=="spam":
        label = "spam"
        predicted_spam = predicted_spam + 1
    if label==actual_file:
        correctly_classified_documents = correctly_classified_documents + 1
        if label=="spam":
            correctly_classified_as_spam = correctly_classified_as_spam + 1
        elif label=="ham":
            correctly_classified_as_ham = correctly_classified_as_ham + 1
    total_documents = total_documents + 1

print("actual_spam" + str(actual_spam))
print("actual_ham" + str(actual_ham))
print ("predicted_spam" + str(predicted_spam))
print("predicted_ham" + str(predicted_ham))
print("correctly_classified_as_ham" + str(correctly_classified_as_ham))
print("correctly_classified_as_spam" + str(correctly_classified_as_spam))


accuracy = correctly_classified_documents / float(total_documents)
precision_spam = correctly_classified_as_spam / float(predicted_spam)
precision_ham = correctly_classified_as_ham / float(predicted_ham)
recall_spam = correctly_classified_as_spam / float(actual_spam)
recall_ham = correctly_classified_as_ham / float(actual_ham)
f1_score_spam = 2 * precision_spam * recall_spam / float(precision_spam + recall_spam)
f1_score_ham = 2 * precision_ham * recall_ham / float(precision_ham + recall_ham)

print ("Accuracy: " + str(accuracy))
print("Precision SPAM: " + str(precision_spam))
print("Precision HAM: " + str(precision_ham))
print("Recall SPAM: " + str(recall_spam))
print ("Recall HAM: " + str(recall_ham))
print("F1 score SPAM: " + str(f1_score_spam))
print("F1 score HAM: " + str(f1_score_ham))