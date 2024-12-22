import csv
from pymongo import MongoClient

client = MongoClient('')
db = client['evault']
collection = db['legal_documents']

with open('legal_documents.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        collection.insert_one(row)

print("Data imported successfully!")
