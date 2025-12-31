import nltk
from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["running", "flies", "studies", "better", "playing", "happiness"]
print("Word\t\tStem")
print("-----------------------")
for word in words:
    print(word, "\t", ps.stem(word))
