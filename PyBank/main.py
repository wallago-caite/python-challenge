#import ways of talking to OS and CSV   
import os
import csv

# Define the relative path to the CSV file
csvpath = "./budget_data.csv"

# Open the CSV file
with open(csvpath, 'r') as csvfile:
   csvReader = csv.reader(csvfile)

#convert to a list and separate the header from the data
   csv_list = list(csvReader)
   csv_data = csv_list[1:]
   number_months = len(csv_data)
 
#set the initial values for the for loop
   csv_header = csv_list[0]
   net_total = 0
   previous_profit_loss = 0
   total_change = 0
   greatest_increase = ["", 0]
   greatest_decrease = ["", 0]

#start that for loop iteration fun!
   for row in csv_data:
#converts p&L strong to integer and sum em- row 1 is the second item in the list within the csv-read list thus 1
      net_total = net_total + int(row[1])
#converts p&L strong to integer and sum em- row 1 is the second item in the list within the csv-read list thus 1

#print the total number of months (aka the total number of list data)
   print("Total Months:"," ",number_months)
   
#print the total amount of profits and losses over the whole period
   print("Total:"," ","net_total")

    
    # average change over the whole period
    #greatest increase in profits date and amount over period
    # greatest decrease in profits date and amount over period
    #print to terminal
    #export a txt file with the results 
