# Import dependencies

import os
import csv
import numpy as np

# Create Path
input_path_2 = os.path.join('..', 'Resources', 'election_data.csv') 

# Open and Read File
with open(input_path_2) as csvfile:

    # CSV reader 
    csvreader_2 = csv.reader(csvfile, delimiter=',')

    print(csvreader_2)

    # Read the header row first
    csv_header_2 = next(csvreader_2)
    print(f"CSV Header: {csv_header_2}")
    
    # Set Variables 
    totalvotes = 0 
    votes = 0
    vote_correy = 0
    vote_li = 0
    vote_otooley = 0
    vote_khan = 0
    
  
    
    candidates = []
    
    
    for row in csvreader_2:
        voterid = row[0]
        county = row[1] 
        candidates.append(row[2])
        totalvotes +=1
        if row[2] == "Correy":
            vote_correy = vote_correy + 1
        elif row[2] == "Li":
            vote_li = vote_li + 1
        elif row[2] == "OTooley":
            vote_otooley = vote_otooley + 1
        elif row[2] == "Khan":
            vote_khan = vote_khan + 1
        
# A complete list of candidates who received votes
# Candidates = Khan, Correy, Li, O'Tooley 
    
    candidates = np.unique(candidates)
    print(candidates)
    
# The total number of votes cast

print(f"Total Votes: {totalvotes}")

#The total number of votes each candidate won

votes = [vote_correy, vote_li, vote_otooley, vote_khan]

print(f"Votes for Correy: {votes[0]}", "Votes for Li: {votes[1]}", "Votes for OTooley: {votes[2]}", "Votes for Khan: {votes[3]}")
      
print(f"Votes_Per_Candidate: {votes}") 

#The percentage of votes each candidate won

Percentage_Correy = (vote_correy / totalvotes) * 100
Percentage_Li = (vote_li / totalvotes) * 100
Percentage_OTooley = (vote_otooley / totalvotes) * 100
Percentage_Khan = (vote_khan / totalvotes) * 100

Percentage_List = [str(round(Percentage_Correy,2)),str(round(Percentage_Li,2)), 
                str(round(Percentage_OTooley,2)), str(round(Percentage_Khan,2))]

print(f"Votes_Percentage: {Percentage_List}") 

#The winner of the election based on popular vote
candidates = ['Correy', 'Li','OTooley','Khan']

Winner = candidates[Percentage_List.index(max(Percentage_List))]
print(f"Election_Winner: {Winner}") 
      
