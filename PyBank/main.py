#import ways of talking to OS and CSV   
import os
import csv

# Define the file paths
filepath = r'./PyBank/Resources/budget_data.csv'
csv_file = 'budget_data.csv'
output_file = 'output.txt'

# Join the file paths
csv_path = os.path.join(filepath, csv_file)
output_path = os.path.join(filepath, output_file)

# Open the CSV file
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_headers = next(csvreader)
    print(csv_headers)  