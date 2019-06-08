import sys
import csv
from querys import userInput
from django.shortcuts import render
from dictionary import dct, id, term
from results import postList

# Create your views here.
comics = []
desc2 = {}
with open('comics.csv', encoding = "utf8") as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        desc = {
            'title': row[1],
            'desc': row[3],
        }
        desc2[row[0]] = {}
        desc2[row[0]]['title'] = row[1]
        desc2[row[0]]['desc'] = row[3]

        comics.append(desc)

def home(request):
    return render(request, 'comic/home.html')

def search(request):
    post = []
    context = {
            'comics': comics
    }
    query = request.GET.get('q')
    if query:
        inputs = userInput(query)
        post = postList(inputs, dct, id, desc2, term)
        context = {
            'comics': post
        }

    return render(request, 'comic/search.html', context)

def description(request):
    return render(request, 'comic/description.html')

def classifier(request):
    return render(request, 'comic/classifier.html')

def stats(request):
    return render(request, 'comic/stats.html')

def recommender(request):
    return render(request, 'comic/recommender.html')
