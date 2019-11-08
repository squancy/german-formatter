# Input formatting program for Loquela
import re

text = open('gerw2.txt', 'r', encoding='utf-16').read()
text = re.sub(r'\s{2,}', '___', text)
result = ''
text = text.replace(',', '')
text = re.split(r'(___|\n)', text)
text = [el for el in text if el != '___' and el != '\n' and el != '']

for i in range(0, len(text) - 1, 2):
	result += text[i] + "#" + text[i + 1] + ','

result = result[:-1]
print(result)
