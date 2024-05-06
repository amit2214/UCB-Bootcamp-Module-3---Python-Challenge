## Challenge 3 - Amit Suresh
## Your task is to create a Python script that analyzes the records to calculate each of the following values:
## PyBank:
import os
print(os.getcwd())
import csv
budget_data = os.path.join ('..\Resources', 'budget_data.csv')
# set path for files:

#Name of output:

Title = 'Financial Analysis'
print(Title)
print('----------------------')

#Text file
text_path = 'Analysis.txt'
outfile = os.path.join('analysis', text_path)

#Set variables:
totalmonths = []
total = []
averagechange = []
greatestprofitincrease = []
greatestprofitdecrease = []

# budget = 'budget_data.csv'
new_var = open('budget_data.csv')
with new_var as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

# profits and date
    for row in csvreader:
        totalmonths.append(row[0])
        total.append(int(row[1]))
for i in range (len(total) - 1):
        averagechange.append(total[i+1] - total[i])

# totals and sums
## The total number of months included in the dataset
total_months = len(totalmonths)
sum_total = sum(total)
average_change = (sum(averagechange) / len(averagechange))
## The net total amount of "Profit/Losses" over the entire period
greatest_profit_increase = ((totalmonths[averagechange.index(max(averagechange))+1]))
greatest_profit_decrease = ((totalmonths[averagechange.index(min(averagechange))+1]))

## The changes in "Profit/Losses" over the entire period, and then the average of those changes
## The greatest increase in profits (date and amount) over the entire period
## The greatest decrease in profits (date and amount) over the entire period
greatest_increase = max(averagechange)
greatest_decrease = min(averagechange)

# output:
output =(
     f'Financial Analysis\n'
     f'----------------------\n'
     f'Total Months: {total_months}\n'
     f'Total Profits: {sum_total}\n'
     f'Average Change: {average_change}\n'
     f'Greatest Profit Increase: {greatest_profit_increase} {greatest_increase}\n'
     f'Greatest Profit Increase: {greatest_profit_decrease} {greatest_decrease}\n'
)