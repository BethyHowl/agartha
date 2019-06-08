from stem import tok, term, numOfDoc, id
import math

def presentCount(term, tok):
	count = 0
	for doc in tok:
		if term in doc:
			count = count + 1
	return count

def termFreq(term, doc):
	count = 0
	for x in doc:
		if term == x:
			count = count + 1
	if count == 0:
		return 0
	return 1 + math.log10(count)

def idfValue(term, pres, num):
	df = pres[term]
	return math.log10(num/(df))

allDict = {}
pres = {}
weight = {}
dct = {}
w = 0
i = 0

for terms in term:
	pres[terms] = presentCount(terms, tok)

#calculating the vector for each document
for doc in tok:
	norm = 0
	dct[i] = {}
	for terms in term:
		w = termFreq(terms, doc) * idfValue(terms, pres, numOfDoc)
		weight[terms] = w
		norm += pow(w,2)

	for terms in term:
		dct[i][terms] = weight[terms]/norm

	i += 1
