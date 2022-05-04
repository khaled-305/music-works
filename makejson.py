import csv
import json
from collections import defaultdict

def convertCSV(csv_path, json_path, model_name):
    jsonData = defaultdict(list)
    entries = []

    with open(csv_path, encoding='utf-8') as csvfile:
        csvData = csv.DictReader(csvfile)

        for rows in csvData:
            #jsonData[rows['title']].append([rows['contributors']].append([rows['iswc']]))
            model = model_name
            fields = rows
            row_dict = {}

            pk = 1

            while pk < len(rows):
                pk = pk + 1

            row_dict['pk'] = int(pk)

            row_dict['model'] = model
            row_dict['fields'] = fields

            entries.append(row_dict)

    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(entries, indent = 4))


# Enter the absolute path of the CSV file
csv_path = r'/Users/chikeziemnwadinobi/Desktop/musicapp/worksapp/fixtures/works_metadata.csv'
# Enter the absolute path of the JSON file
json_path = r'/Users/chikeziemnwadinobi/Desktop/musicapp/worksapp/fixtures/works_metadata.json'

convertCSV(csv_path, json_path, 'worksapp')