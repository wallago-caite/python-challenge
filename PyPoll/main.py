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
   total_votes = len(csv_data)
 
   #set the initial values for the for loop
   candidate_name = [item[2] for item in csv_data]

#store as string print the grand totals to the terminal using string replacement C method
output = total_votes

#print to the terminal
print(output)

#make a file in my main
output_file = "./output.txt"

#open the file as writeable ('w')and write the output into the the txtfile  
with open(output_file,'w') as txtfile:
    txtfile.write(output)

#Module is finished!!!! YAHHHHHHHHH