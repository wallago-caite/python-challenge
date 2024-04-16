#import ways of talking to OS and CSV   
import os
import csv

# Define the relative path to the CSV file
csvpath = "./Resources/budget_data.csv"

# another way of doing this is : os.path.join("Resources","budget_data.csv")

# Open the CSV file
with open(csvpath, 'r') as csvfile: # csvreader has a (csv, 'r' UTF<<path code that fixes coding errors)
   csvReader = csv.reader(csvfile)

   #convert to a list and separate the header from the data
   csv_list = list(csvReader)
   csv_header = csv_list[0] #another way of doing this is csv_header = next(csvReader)
   csv_data = csv_list[1:]
   
   # total the number of months
   number_months = len(csv_data)
 
   #set the initial values for the for loop
   net_total = 0
   prior_profit_loss = 0
   total_change = 0
   greatest_increase = ["", 0]
   greatest_decrease = ["", 0]
   change = 0

#start that for loop iteration fun! We start in csv_data because that is a list separated from the header row 
# csv_data only contains only data

for row in csv_data:
   #converts p&L string to integer.  Sums the second items in the the list after this conversion
   try:
      profit_loss = int(row[1])
   except ValueError:#kept getting zero-based error, so added an error check with GPT help... 
      # Skip rows with non-numeric values
      continue
   net_total = net_total + profit_loss

   #find total change by starting at row 2 
   # (basically we finding prior_profit_loss after 0) and finding change of 1 to 2, 2 to 3, 3 to 4etc
   # this sums these derivative #s of the original data points
   if prior_profit_loss != 0:
      change = profit_loss - prior_profit_loss
      total_change = total_change + change

   #find greatest increase $ decrease
   #remember that change is the change between points in the second column
   # so when that is calculated, we can compare to row 0, 1, 2, 3 etc
      if change > greatest_increase[1]:         
            greatest_increase = [row[0], change]
      elif change < greatest_decrease[1]:
            greatest_decrease = [row[0], change]

   #reset prior so that it is the new current profit loss
   prior_profit_loss = profit_loss

#calculate the average profit note that number of months is based on the in between moment, so it will be -1 since month one is a given
average_change = round(total_change / (number_months - 1))

#store as string print the grand totals to the terminal using string replacement C method
output = """
Financial Analysis\n
------------------------\n
Total Months: %d\n
Total: %d\n
Average Change: $%d\n
Greatest Increase: %s\n
Greatest Decrease: %s\n
""" % (number_months,net_total,average_change, str(greatest_increase),str(greatest_decrease))
#another way of doing this is with an FSTRING f' with these inside of the code  

#print to the terminal
print(output)

#make a file in my subsidiary folder
output_file = "./analyis/output.txt"

#open the file as writeable and write the output into the the txtfile  
# another way of doing this is : os.path.join("Resources","budget_data.csv")
with open(output_file,'w') as txtfile: #can also add to a text file with an "encoding" parameter
    txtfile.write(output)

#Celebrate!! Half the module is done!!!