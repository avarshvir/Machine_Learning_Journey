# Build the dictionary once and reuse it
LEMMA_DICT = {
    'is': 'be', 'am': 'be', 'are': 'be', 'was': 'be', 'were': 'be',
    'studies': 'study', 'studying': 'study', 'studied': 'study',
    'better': 'good', 'cars': 'car', 'geese': 'goose',
    'children': 'child', 'men': 'man', 'women': 'woman'
}

def efficient_lemmatizer(word):
    return LEMMA_DICT.get(word, word)  # Simple O(1) lookup

# Usage
words = ['is', 'studied', 'studies', 'studying', 'cars', 'better']
lemmas = [efficient_lemmatizer(w) for w in words]
print(list(zip(words, lemmas)))