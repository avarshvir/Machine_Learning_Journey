from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

text = "This is a simple example to demonstrate the use of built-in stopwords in the word cloud."

# Use built-in stopwords
stopwords = set(STOPWORDS)

wordcloud = WordCloud(stopwords=stopwords, background_color='white').generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
#--------------------------------------------------------------------
print(STOPWORDS)
#--------------------------------------------------------------------
#Add more stopwords
stopwords = set(STOPWORDS)
stopwords.update(["example", "simple"])
#--------------------------------------------------------------------
#Remove a Word from Stopwords
stopwords = set(STOPWORDS)
stopwords.discard("the")