import os
import csv
from statistics import mean

filepath = os.path.join("C:/","Users/","rapon/","Documents/","Python Scripts/","CSV/", "budget_data_1.csv")
newfile = os.path.join("C:/","Users/","rapon/","Documents/","Python Scripts/","CSV/", "PyBankResults.txt")


with open(filepath) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    storage = {} # dictionary for keeping data from csv file, Date-keys; Revenue-values
    monthChange = [] # list for keeping change in revenue between months
    final = {} # dictionary for keeping Data: Change in revenue monthly
    answer = [] # list for answer lines
    for row in reader:
        if row[0]!= "Date": #Exclude the first row
            storage[row[0]] = int(row[1])
    totalMonth = len(storage) # Number of month = number of keys
    totalRevenue = sum(storage.values()) # Sum of all values = total revenue for the period
    revs = tuple(storage.values()) #Revenue Values immutable for finding average change
    month = tuple(storage.keys()) #Date keys immutable for finding average change 

    for x in range(1, (len(revs))): # Create a list of revenue changes
        monthChange.append((int(revs[x]) - int(revs[x-1])))

    average = round(mean(monthChange)) # Average change in revenue between months

    for x in range(1, (len(month))): # Create a final dictionary
        final[month[x]] = int(monthChange[x-1])

    maxIncrease = max(zip(final.values(), final.keys()))
    minDecrease = min(zip(final.values(), final.keys()))

    answer.append('Financial Analysis')
    answer.append('----------------------------')
    answer.append('Total Months: ' + str(totalMonth))
    answer.append('Total Revenue: $' + str(totalRevenue))
    answer.append('Average Revenue Change: $' + str(average))
    answer.append('Greatest Increase in Revenue: ' + str(maxIncrease[1]) + ' ($' + str(maxIncrease[0]) + ')')
    answer.append('Greatest Decrease in Revenue: ' + str(minDecrease[1]) + ' ($' + str(minDecrease[0]) + ')')

    # Print an answer, each element from new line
    print("\n".join((answer)))

# Export answer to txt file
with open(newfile, 'w') as txtfile:
    txtfile.write('\n'.join(answer))