# Input formatting program for Loquela
import re

def format():
	filePath = str(input('Enter file to format: '))
	try:
		text = open(filePath, 'r', encoding='utf-16').read()
	except:
		print('Wrong file path given')
		return 'Error occurred'

	text = re.sub(r'\s{2,}', '___', text)
	# remove example sentences
	text = re.sub(r'[A-Z][a-z ]*\w*(\.|\?|\!)', '', text)
	result = ''
	text = text.replace(',', '')
	text = re.split(r'(___|\n)', text)
	text = [el for el in text if el != '___' and el != '\n' and el != '']

	for i in range(0, len(text) - 1, 2):
		result += text[i] + "#" + text[i + 1] + ','

	result = result[:-1]
	print(result)
	return 'Success'

call = format()
if call != 'Success':
	while call != 'Success':
		call = format()

	
