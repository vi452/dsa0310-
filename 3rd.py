def stem(word):
    suffixes = ["ing", "ed", "es", "s"]
    for suffix in suffixes:
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            return word[:-len(suffix)]
    return word
def lemmatize(word):
    lemma_dict = {
        "cars": "car",
        "children": "child",
        "mice": "mouse",
        "better": "good",
        "running": "run",
        "flies": "fly",
        "studies": "study"
    }
    return lemma_dict.get(word, word)
words = ["running", "cars", "better", "flies", "studies", "children"]
print("Word\t\tStem\t\tLemma")
print("--------------------------------------")
for w in words:
    print(f"{w}\t\t{stem(w)}\t\t{lemmatize(w)}")
