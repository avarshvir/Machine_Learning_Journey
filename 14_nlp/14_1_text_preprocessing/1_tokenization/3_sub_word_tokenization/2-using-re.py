import re

def regex_subword_tokenizer(text):
    pattern = re.compile(r'(un|re|in|able|ing|ly)')
    tokens = []
    for word in text.split():
        parts = pattern.split(word)
        tokens.extend([p for p in parts if p])
    return tokens

text = "Tokenization helps understanding unbreakable words"
print(regex_subword_tokenizer(text))