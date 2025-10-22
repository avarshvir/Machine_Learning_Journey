def generate_ngrams(text, n):
    words = text.split()
    return [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]

text = "Machine Learning is Powerful"
print(generate_ngrams(text, 2))
print("---------------------------")
print(generate_ngrams(text, 3))
