import re
text = "Hello World! NLP is fun."
words = re.findall(r'\b\w+\b', text)
print(words) # Output: ['Hello', 'World', 'NLP', 'is', 'fun']
