import string

print(string.punctuation)

text = "Messi is great player. However, he is yet to win a world cup"
text_p = "".join([char for char in text if char not in string.punctuation])
print(text_p)