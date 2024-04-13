#import ways of talking to OS and CSV   
import os
import csv

# Define the relative path to the CSV file
csvpath = "./budget_data.csv"

# Open the CSV file
with open(csvpath, 'r') as csvfile:
   csvReader = csv.reader(csvfile)
   csv_list = list(csvReader)

   for row in csv_list:


    # loop through and find total months
    # total amount of profit/losses over the whole period
    # average change over the whole period
    #greatest increase in profits date and amount over period
    # greatest decrease in profits date and amount over period
    #print to terminal
    #export a txt file with the results 
