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
   csv_header = csv_list[0]
   csv_data = csv_list[1]
   number_months = len(csv_data)
 
#set the initial values for the for loop
   net_total = 0
   prior_profit_loss = 0
   total_change = 0
   greatest_increase = ["", 0]
   greatest_decrease = ["", 0]
   change = 0

#start that for loop iteration fun! We start in csv_data because that is a list separated from the header row it contains only data
   for row in csv_data:
#converts p&L string to integer.  Sums the second items in the the list after this conversion
      profit_loss = int(row[1])
      net_total = net_total + profit_loss

#find total average change by starting at row 2 (basically prior after 0) and finding change of 1 to 2, 2 to 3, 3 to 4, and summing these derivative #s
   if prior_profit_loss != 0:
            change = profit_loss - prior_profit_loss
            total_change = total_change + change

#find greatest increase $ decrease, remember that change is the change between points in the second column, so when that is calculated, we can compare to row 0, 1, 2, 3 etc
            greatest_increase = [row[0], change]
   elif change < greatest_decrease[1]:
            greatest_decrease = [row[0], change]

#reset prior so that it is the new current profit loss
prior_profit_loss = profit_loss

#calculate the average profit
average_change = total_change / number_months
#print the total number of months (aka the total number of list data)
   print("Total Months:"," ",number_months)

#print the total amount of profits and losses over the whole period
   print("Total:"," ",net_total)

#print average change over the whole period
   print("Average Change:"," ",total_change)

#print greatest increase
   print("Greatest Increase:"," ",greatest_increase)

#print greatest decrease
   print("Greatest Decrease:"," ",greatest_decrease)

#export a txt file with the results