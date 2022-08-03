#!/usr/bin/python

import sys,csv

from xlsx2csv import Xlsx2csv

Xlsx2csv(str(sys.argv[1]), outputencoding="utf-8").convert("myfile.csv",sheetname="Joins")

print ('Total number of arguments:', format(len(sys.argv)))

# opening the CSV file
with open('myfile.csv', mode ='r')as file:

# reading the CSV file
    csvFile = csv.reader(file)

# displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)
