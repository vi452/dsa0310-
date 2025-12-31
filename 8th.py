
train = [
    ("the", "DT"), ("dog", "NN"), ("dog", "NN"),
    ("runs", "VB"), ("runs", "VB"),
    ("a", "DT"), ("cat", "NN")
]

counts = {}
for w, t in train:
    counts.setdefault(w, {})
    counts[w][t] = counts[w].get(t, 0) + 1
def pos_tag(sentence):
    result = []
    for word in sentence.split():
        if word in counts:
            tag = max(counts[word], key=counts[word].get)
        else:
            tag = "NN"   # default
        result.append((word, tag))
    return result
sentence = "the dog runs"
print(pos_tag(sentence))
