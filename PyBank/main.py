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
   csv_data = csv_list[1:]
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
   try:
      profit_loss = int(row[1])
   except ValueError:
      # Skip rows with non-numeric values
      continue
   net_total = net_total + profit_loss

   #find total average change by starting at row 2 (basically prior after 0) and finding change of 1 to 2, 2 to 3, 3 to 4, and summing these derivative #s
   if prior_profit_loss != 0:
      change = profit_loss - prior_profit_loss
      total_change = total_change + change

   #find greatest increase $ decrease, remember that change is the change between points in the second column, so when that is calculated, we can compare to row 0, 1, 2, 3 etc
      if change > greatest_increase[1]:         
            greatest_increase = [row[0], change]
      elif change < greatest_decrease[1]:
            greatest_decrease = [row[0], change]

   #reset prior so that it is the new current profit loss
   prior_profit_loss = profit_loss

#calculate the average profit note that number of months is based on the in between moment, so it will be -1 since month one is a given
average_change = total_change / (number_months - 1)

#store as string print the grand totals to the terminal using string replacement C method
output = """
Total Months: %d
Total: %d
Average Change: %d
Greatest Increase: %s
Greatest Decrease: %s
""" % (number_months,net_total,total_change, str(greatest_increase),str(greatest_decrease))

#print to the terminal
print(output)

#make a file in my main
output_file = "./output.txt"

#open the file as writeable and write the output into the the txtfile  
with open(output_file,'w') as txtfile:
    txtfile.write(output)

#Celebrate!! Half the module is done!!!