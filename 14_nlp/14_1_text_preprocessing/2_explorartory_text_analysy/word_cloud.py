from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "My name is Arshvir. I am an AI Engineer who love AI, ML, Robotics, Embedded System."

wc = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
