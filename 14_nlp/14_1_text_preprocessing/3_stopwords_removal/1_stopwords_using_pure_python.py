stopwords = set(["the","is", "in", "and", "to", "of"])
sentence = "The cat is sitting on the mat and looking at the sky."

tokens = sentence.lower().split()
print(tokens)

filtered_tokens = []
for word in tokens:
    if word not in stopwords:
        filtered_tokens.append(word)

print(filtered_tokens)

filtered_tokens2 = [word2 for word2 in tokens if word2 not in stopwords]
print(filtered_tokens2)
