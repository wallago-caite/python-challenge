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




#Results
print("Election Results")
print("------------------")

#total vote line
print ("Total Votes")
print (total_votes)
print ("-----------------")

#print candidate line 

# print winner line

#export to txt file