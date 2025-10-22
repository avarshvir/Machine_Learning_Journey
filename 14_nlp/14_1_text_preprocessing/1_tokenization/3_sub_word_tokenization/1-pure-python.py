def simple_subword_tokenizer(text):
    subwords = []
    for word in text.split():
        if len(word) > 6:
            subwords.append(word[:3])
            subwords.append(word[3:])
        else:
            subwords.append(word)
    return subwords

text = "Tokenization helps understanding unbreakable words"
print(simple_subword_tokenizer(text))



            