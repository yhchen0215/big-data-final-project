import json, csv

INPUT_FILE = 'data/avian_influenza_raw.json'
OUTPUT_FILE = 'data/AVIAN_INFLUENZA.csv'

f = open(INPUT_FILE, encoding="utf-8")
dataFromJson = json.load(f)
dataToCsv = []

for row in dataFromJson:
    for year in list(row.keys()):
        if str(year).isnumeric():
            dataToCsv.append([str(year) + str(row['month'])[:-1].zfill(2), row[year]])

with open(OUTPUT_FILE, 'w', encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['month', 'amount'])
    writer.writerows(dataToCsv)