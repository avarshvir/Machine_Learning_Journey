def simple_lemmatizer(word):
    word_groups = {
        'be': ['is', 'am', 'are', 'was', 'were', 'being', 'been'],
        'study': ['studies', 'studying', 'studied'],
        'go': ['goes', 'going', 'went', 'gone'],
        'good': ['better', 'best'],
        'car': ['cars'],
        'goose': ['geese'],
        'child': ['children']
    }

    lemma_dict = {}
    for lemma, forms in word_groups.items():
        lemma_dict[lemma] = lemma
        for form in forms:
            lemma_dict[form] = lemma
    
    return lemma_dict.get(word, word)

# Test the improved versions
words = ['is', 'studied', 'studies', 'studying', 'cars', 'better', 'geese', 'children']
print("Dictionary-based:")
lemmas1 = [simple_lemmatizer(w) for w in words]
print(list(zip(words, lemmas1)))

print("\nList-based:")
lemmas2 = [simple_lemmatizer(w) for w in words]
print(list(zip(words, lemmas2)))

print(simple_lemmatizer("went"))