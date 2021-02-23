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
