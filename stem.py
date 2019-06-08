import csv
import nltk
import sys
import re

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

document = []
tok = []
term = []
id = {}
numOfDoc = 0

#tokening
with open('stopWord.txt', 'r') as stopWords:
	stop = stopWords.read().split( '\n' )

stopWords.close()

with open('comics.csv', encoding = "utf8") as csvFile:
	csvReader = csv.reader(csvFile)
	for row in csvReader:
		docTok = []
		id[numOfDoc] = row[0]
		numOfDoc = numOfDoc + 1
		for termTitle in row[1].split():
			if termTitle not in stop:
				if not re.search(r'\d', termTitle):
					termTitle = stemLemma(termTitle.lower())
					docTok.append(termTitle)
					if termTitle not in term:
						term.append(termTitle)
		for termDoc in row[3].split():
			if not row[3]:
				continue
			if termDoc not in stop:
				if not re.search(r'\d', termDoc):
					termDoc = stemLemma(termDoc.lower())
					docTok.append(termDoc)
					if termDoc not in term:
						term.append(termDoc)

		tok.append(docTok)

csvFile.close()
