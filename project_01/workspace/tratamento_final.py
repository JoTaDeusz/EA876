#! /usr/bin/env python3

import csv 
import sys 

try:
    input_file = sys.argv[1]

except:
    print('Usage: data_base.csv')
    exit()

# itera nas linhas da entrada padrao
for line in sys.stdin:
    fields = line.split('-')
    fields[3] = fields[3].rstrip()  # retira '\n' do final
    fields[2].replace(',', '.')
    fields[3].replace(',', '.')
    with open(input_file, newline='') as csv_file:
        database = csv.reader(csv_file, delimiter=',', quotechar='"')
        # itera nas linhas do csv
        for row in database:
            if fields[0] == row[1]:
                fields[0] = row[0]
            if fields[1] == row[1]:
                fields[1] = row[0]
    print(fields[0] + "," + fields[1] + "," + fields[2] + "," + fields[3])
