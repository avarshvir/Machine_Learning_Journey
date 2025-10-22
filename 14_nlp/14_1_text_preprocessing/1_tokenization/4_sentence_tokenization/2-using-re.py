import re

def regex_sentence_tokenizer(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    return sentences

text = "AI evolves fast. NLP is part of it! Are you learning it?"
print(regex_sentence_tokenizer(text))
