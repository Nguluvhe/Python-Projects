import csv

with open('/home/infbr003/Downloads/Titan_Pricefile_MV.csv', mode='r', newline='', encoding='utf-8') as f1:
    file1_reader = csv.DictReader(f1, delimiter='\t')
    file1_data = list(file1_reader)
