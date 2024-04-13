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

#set inital values for a for loop
# we have to find the total # of votes per candidate with requires us to first
#find vote total and pair to a candidate like we did in vba
#find the % of the total votes for that candidate
# find the max total number of votes for that candidate

#find initial values
candidate_votes = []
candidate_percent = []
candidate_location = [2] #where candidate is within the row (or rather list item)
candidates = [] #list of  candidates


for entry in csv_data:
   candidate = entry[2] #candidate is at 3rd index location
   if candidate not in candidates:
      candidates= candidates + [candidate] #add new unique candidate to list of candidates. 

#vote count for each candidate starts at 0
votes = [0] * len(candidates)

for entry in csv_data:
   candidate = entry[2]
   index = candidates.index(candidate)
   votes[index] = votes[index] +1

######################################################
#Results
print("Election Results")
print("------------------")

#total vote line
print ("Total Votes")
print (total_votes)
print ("-----------------")

# Find % and winner -- Print the total number of votes per candidate
max_votes = 0
winner_list = 0

for i in range(len(candidates)):
   percentage = (votes[i] / total_votes) * 100
   candidate_percent.append(percentage)
   if votes[i] >max_votes:
      max_votes = votes[i]
      winner_list = i

   print(candidates[i] + " " + str(votes[i]))


# print winner line

#export to txt file