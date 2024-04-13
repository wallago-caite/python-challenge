#import ways of talking to OS and CSV   
import os
import csv

# Define the relative path to the CSV file
csvpath = "budget_data.csv"

# Open the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_headers = next(csvreader)
    print(csv_headers)





