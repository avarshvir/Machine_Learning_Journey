import re

def regex_ngrams(text, n):
    words = re.findall(r'\b\w+\b', text.lower())
    return [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]

text = "Natural language processing with Python is amazing!"
print(regex_ngrams(text, 3))  # Trigrams
