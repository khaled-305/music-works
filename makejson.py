import csv
import json
from collections import defaultdict

def convertCSV(csv_path, json_path):
    jsonData = defaultdict(list)
    entries = []

    with open(csv_path, encoding='utf-8') as csvfile:
        csvData = csv.DictReader(csvfile)

        for rows in csvData:
            jsonData[rows['title']].append([rows['contributors']].append([rows['iswc']]))


   
    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(jsonData, indent = 4))

csv_path = r'/Users/chikeziemnwadinobi/Desktop/musicapp/worksapp/fixtures/works_metadata.csv'
json_path = r'/Users/chikeziemnwadinobi/Desktop/musicapp/worksapp/fixtures/works_metadata.json'

convertCSV(csv_path, json_path)