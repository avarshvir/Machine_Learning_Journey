from gensim.parsing.preprocessing import remove_stopwords

text = "Messi is great player. However, he is yet to win a world cup"
sentence = remove_stopwords(text)

print(sentence)


#Messi great player. However, win the world cup
