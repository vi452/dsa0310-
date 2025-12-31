def pos_tag(word):
    if word.lower() in ["the", "a", "an"]:
        return "DT"         
    elif word.lower() in ["is", "are", "was", "were", "be"]:
        return "VB"         
    elif word.lower().endswith("ing"):
        return "VBG"         
    elif word.lower().endswith("ed"):
        return "VBD"         
    elif word.lower().endswith("ly"):
        return "RB"        
    elif word.lower() in ["quick", "brown", "lazy", "interesting"]:
        return "JJ"          
    elif word.lower() in ["in", "on", "over", "under"]:
        return "IN"         
    else:
        return "NN"          
text = "The quick brown fox is running quickly"
words = text.split()
print("Word\t\tPOS Tag")
print("-------------------------")
for word in words:
    print(word, "\t\t", pos_tag(word))
