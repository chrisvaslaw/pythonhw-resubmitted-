# pythonhw-resubmitted-
# Import dependencies
import os
import csv

# Create Path
input_path = os.path.join('..', 'Resources', 'budget_data.csv') 

# Open and Read File
with open(input_path) as csvfile:

# CSV reader 
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)


# Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
# Store Variables
    months = []
    profit = [] 
    change_in_profit = []
    

# Read each row of data after the header
    for row in csvreader:
        print(row)
        months.append(row[0])
        profit.append(int(row[1]))



# The total number of months included in the dataset
print(f"Total_Months: {len(months)}") 

# The net total amount of "Profit/Losses" over the entire period    
print(f"Total_Profit: ${sum(profit)}")


# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

for p in range(len(profit)-1):
    change_in_profit.append(profit[p+1]-profit[p])
    
    
print(f"Average Change: {round(sum(change_in_profit)/len(change_in_profit),2)}") 

# The greatest increase in profits (date and amount) over the entire period

greatest_increase = max(change_in_profit)
greatest_increase_month = change_in_profit.index(max(change_in_profit)) + 1
print(f"Greatest_Increase: {months[greatest_increase_month]}")
      
# The greatest decrease in losses (date and amount) over the entire period

greatest_decrease = min(change_in_profit)
greatest_decrease_month = change_in_profit.index(min(change_in_profit)) + 1
print(f"Greatest_Decrease: {months[greatest_decrease_month]}")
_____________________________________________________________________________________________________________________________________________________________________________
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
      
