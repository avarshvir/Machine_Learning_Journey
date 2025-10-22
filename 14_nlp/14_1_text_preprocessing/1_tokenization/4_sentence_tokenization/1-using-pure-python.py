def sentence_tokenize_basic(text):
    sentences = text.replace('!','.').replace('?','.').split('.')
    return [s.strip() for s in sentences if s.strip()]

text = "Artificial Intelligence is fascinating. Machine learning is powerful! NLP is growing?"
print(sentence_tokenize_basic(text))