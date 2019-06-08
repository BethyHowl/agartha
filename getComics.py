import csv
import sys

comics = []

with open('userInput.txt', encoding = "utf8") as txtFile:
    txtReader = txtFile.read()
    if not txtReader:
        with open('comics.csv', encoding = "utf8") as csvFile:
            csvReader = csv.reader(csvFile)
            for row in csvReader:
                desc = {
                    'id': row[0],
                    'title': row[1],
                    'desc': row[3],
                }
            comics.append(desc)
    else:
        comics.append(txtReader)
