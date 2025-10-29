# BASIC MANUAL LEMMATIZATION (rule-based example)

def simple_lemmatizer(word):
    # very simple rule-based mapping
    irregulars = {
        'is': 'be', 'am': 'be', 'are': 'be', 'was': 'be', 'were': 'be',
        'studies': 'study', 'studying': 'study', 'studied': 'study',
        'better': 'good', 'cars': 'car', 'geese': 'goose'
    }

    # if in irregular dictionary, return lemma
    if word in irregulars:
        return irregulars[word]

    # typical rule for regular plurals ending in 's'
    if word.endswith('s') and len(word) > 3:
        return word[:-1]

    # words ending with 'ing', 'ed'
    elif word.endswith('ing'):
        return word[:-3]
    elif word.endswith('ed'):
        return word[:-2]

    return word  # unchanged if no rule applies

# try it!
words = ['is', 'studied', 'studies', 'studying', 'cars', 'better']
lemmas = [simple_lemmatizer(w) for w in words]
print(list(zip(words, lemmas)))
