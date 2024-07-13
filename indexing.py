# -------------------------------------------------------------------------
# AUTHOR: Luis Dominguez
# FILENAME: Indexing
# SPECIFICATION: python program used to exercise information retrieval
# FOR: CS 4250- Assignment #1
# TIME SPENT: 1 hr
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to
# work here only with standard arrays

# Importing some Python libraries
import csv
import re

documents = []

# Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        word = row[0].split(' ')
        if i > 0:  # skipping the header
            documents.append(word)
words = []
# print(documents)

for i in range(len(documents)):
    for j in documents[i]:
        words.append(j)

# print(words)
# Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.
# --> add your Python code here

stopWords = {'you', 'i', 'her', 'she', 'it', 'we', 'they', 'their', 'but', 'and', 'or'}
new_arr = []

for i in words:
    if i.lower() not in stopWords:
        new_arr.append(i)

# print(new_arr)
# Conducting stemming. Hint: use a dictionary to map word variations to their stem.
# --> add your Python code here
stemming = {re.sub(r's', '', stem): (stem + 's') for stem in new_arr}
print(stemming)

# Identifying the index terms.
# --> add your Python code here
terms = [i for i in stemming]


# Building the document-term matrix by using the tf-idf weights.
# --> add your Python code here
def tf(t, d):
    freq = 0
    for j in range(len(d)):
        if t == d[j] or t == re.sub(r's', '', d[j]):
            freq += 1

    return round(freq / len(d), 4)


freq = []
for i in terms:
    freq.append(tf(i, words))

docTermMatrix = dict(zip(terms, freq))

# Printing the document-term matrix.
# --> add your Python code here
for i in docTermMatrix:
    print(i, end=" ")
    print(docTermMatrix[i])

