#import ways of talking to OS and CSV   
import os
import csv

# Define the relative path to the CSV file
csvpath = "./budget_data.csv"

# Open the CSV file
with open(csvpath, 'r') as csvfile:
   csvReader = csv.reader(csvfile)
   csv_list = list(csvReader)
   number_months = len(csv_list)
   csv_header = csv_list[0]
   net_total = 0
   net_total = sum(csv_list[1:])
   
#start that for loop iteration fun!
   for row in csvlist:
      net_total = net_total+ int(row[1])
#converts p&L strong to integer and sum em- row 1 is the second item in the list within the csv-read list thus 1

   print("Total Months:"," ",number_months)
   Print("Total:"," ","net_total")

    

    # loop through and find total months
    # total amount of profit/losses over the whole period
    # average change over the whole period
    #greatest increase in profits date and amount over period
    # greatest decrease in profits date and amount over period
    #print to terminal
    #export a txt file with the results 
