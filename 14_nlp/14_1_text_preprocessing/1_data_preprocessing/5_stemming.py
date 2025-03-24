import re

text = ['laziness', 'friendly', 'sleeping', 'friendship','faster']
stems = [
    
    re.sub(r'less|ship|ing|les|ly|es|ness|er', '', word) 
    for word in text
]

print(stems)
