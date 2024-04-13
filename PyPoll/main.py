#import ways of talking to OS and CSV   
import os
import csv

# Define the relative path to the CSV file
csvpath = "./election_data.csv"

# Open the CSV file
with open(csvpath, 'r') as csvfile:
   csvReader = csv.reader(csvfile)

   #convert to a list and separate the header from the data
   csv_list = list(csvReader)
   csv_header = csv_list[0]
   csv_data = csv_list[1:]
   number_months = len(csv_data)
 
   #set the initial values for the for loop
   total_votes = 0
   
#start that for loop iteration fun! We start in csv_data because that is a list separated from the header row it contains only data
for row in csv_data:
    
#total votes cast

#list of candidates that received votes in column 1
#percentage of votes each of these candidates received in column 2
#Total number of volumes each candidate won in column 3

#winner of the election based on popular vote

#store as string print the grand totals to the terminal using string replacement C method
    output = """
Election Results
------------------------
Total votes: %d
------------------------
Candidates+%+totals: %d<< this may fail
------------------------
Winner: %s
""" % (total_votes,candidates,winner)

#print to the terminal
print(output)

#make a file in my main
output_file = "./output.txt"

#open the file as writeable ('w')and write the output into the the txtfile  
with open(output_file,'w') as txtfile:
    txtfile.write(output)

#Module is finished!!!! YAHHHHHHHHH