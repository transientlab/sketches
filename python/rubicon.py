import csv, json, ldap3
import os

print('start')

data_folder = 'data'
csv_file_path = os.path.join(data_folder, 'dataFeb-2-2017.csv')
json_file_path = os.path.join(data_folder, 'dataFeb-2-2017.json')
ldif_file_path = os.path.join(data_folder, 'dataFeb-2-2017.ldif')

with open(csv_file_path) as csv_file_handle:
    csv_reader = csv.reader(csv_file_handle)
    for row in csv_reader:
        print(','.join(row))

