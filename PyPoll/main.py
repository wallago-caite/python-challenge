#import ways of talking to OS and CSV   
import os
import csv

# Define the relative path to the CSV file
csvpath = "./Resources/election_data.csv"

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
candidate_votes = []#list starting at zero   
candidate_percent = []#list starting at zero
candidate_location = [2] #where candidate is within the row (or rather list item)
candidates = [] #list of  candidates


for entry in csv_data:
   candidate = entry[2] #candidate is at 3rd index location 3-1 = 2
   if candidate not in candidates:
      candidates= candidates + [candidate] #add new unique candidate to list of candidates. 

#vote count for each candidate starts at 0
votes = [0] * len(candidates) #votes are a list

for entry in csv_data:
   candidate = entry[2] #entries are a list
   index = candidates.index(candidate)
   votes[index] = votes[index] +1

######################################################
#Results

# Find % and winner -- Print the total number of votes per candidate
# requires finding the max votes and creating a list of winners or rather list of tests for winners 
max_votes = 0
winner_list = 0

#set up like vba lottery winning
for i in range(len(candidates)): #dynamic range based on the number of unique candidates found above
   percentage = (votes[i] / total_votes) * 100
   candidate_percent.append(percentage)
   if votes[i] >max_votes:
      max_votes = votes[i]
      winner_list = i # resets the iteration 

# printing to an output line the candidate lines
candidate_output = ""
for i in range(len(candidates)):
    candidate_line = candidates[i] + ": " + str(round(candidate_percent[i], 3)) + "% (" + str(votes[i]) + ")\n"
    candidate_output = candidate_output + candidate_line

#collate outputs
output = """
Election Results \n
------------------------------\n
Total Votes: %d\n
------------------------------\n
%s\n
------------------------------\n
Winner: %s\n
------------------------------\n

""" % (total_votes, candidate_output, candidates[winner_list],)
#can also be done as an f-string..... probably a better solution but if it ain't broke.... 

#print to the terminal
print(output)

#make a file in my main
output_file = "./analysis/output.txt"

#open the file as writeable and write the output into the the txtfile  
with open(output_file,'w') as txtfile:
    txtfile.write(output)

#Celebrate!! Module is complete!!!!