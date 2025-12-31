import random
text = "the cat sat on the mat the cat ate fish"
words = text.split()
bigrams = {}
for i in range(len(words) - 1):
    w1 = words[i]
    w2 = words[i + 1]
    if w1 not in bigrams:
        bigrams[w1] = []
    bigrams[w1].append(w2)
def generate_text(start_word, length=10):
    current_word = start_word
    result = [current_word]
    for _ in range(length - 1):
        next_words = bigrams.get(current_word)
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
        current_word = next_word
    return " ".join(result)
print("Generated Text:")
print(generate_text("the", 10))
