import os
import csv
csvpath = os.path.join("./budget_data.csv")
csvoutput = os.path.join("output.txt")
with open('./budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_headers = next(csvreader)
    print(csvheaders)