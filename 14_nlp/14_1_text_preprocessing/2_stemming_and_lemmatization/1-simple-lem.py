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
    
print(simple_lemmatizer("is"))

irregulars = {
        'is': 'be', 'am': 'be', 'are': 'be', 'was': 'be', 'were': 'be',
        'studies': 'study', 'studying': 'study', 'studied': 'study',
        'better': 'good', 'cars': 'car', 'geese': 'goose'
    }

print(irregulars['better'])