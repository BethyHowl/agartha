import math
import sys
import csv
from operator import itemgetter

def postList(query, dct, id, desc2, docTerm):
    i = 0
    index = {}
    list = []
    post = []
    comics = []

    with open('terms.txt', 'r') as termWords:
    	terms = termWords.read().split( '\n' )

    for doc in dct:
        p = 0
        for term in terms:
            if term not in docTerm:
                continue
            else:
                if not term:
                    continue
                else:
                    p += query[term] + dct[i][term]

        list.append((i,p))
        i += 1

    list.sort(key=itemgetter(1), reverse=True)

    for x in range(10):
        if list[x][1] != 0:
            post.append(id[list[x][0]])

    for identity in post:
        desc = {
           'title': desc2[identity]['title'],
           'desc': desc2[identity]['desc'],
        }
        comics.append(desc)
    return comics
