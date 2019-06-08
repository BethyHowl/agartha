import nltk
import math
from nltk.stem import PorterStemmer

def deleteLetters(text):
	result = []
	if text.startswith('-'):
		text = text.strip('-')
	for letter in text:
		if letter.lower() not in '?(!).,/&;*”“":<>{}':
			result.append(letter.lower())
	return ''.join(result)

def stemLemma(text):
	porter = PorterStemmer()
	text = deleteLetters(text)
	text = porter.stem(text)

	if text.endswith('\''):
		text = text.strip('\'')

	return text

def termFreq(term, doc):
	count = 0
	for x in doc:
		if term == x:
			count = count + 1

	if count == 0:
		return 0

	return 1 + math.log10(count)

def userInput(str):
	q = []
	terms = []
	query = {}
	norm = 0
	weight = {}

	with open('stopWord.txt', 'r') as stopWords:
		stop = stopWords.read().split( '\n' )

	stopWords.close()

	for term in str.split():
		term = stemLemma(term)
		q.append(term)
		if term not in terms:
			if term not in stop:
				terms.append(term)

	for y in terms:
		weight = termFreq(y, q)
		norm += math.pow(weight, 2)

	norm = math.sqrt(norm)

	for y in terms:
	    query[y] = weight/norm

	with open('terms.txt', 'w') as filehandle:
		for item in terms:
			filehandle.write("%s\n" % item)

	return query
