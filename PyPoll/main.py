import os
import csv
from collections import Counter

filepath = os.path.join("C:/","Users/","rapon/","Documents/","Python Scripts/","CSV/","election_data_1.csv")
newfile = os.path.join("C:/","Users/","rapon/","Documents/","Python Scripts/","CSV/","election_results_1.txt")

with open(filepath, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    next(reader, None)

    votesCount = Counter() #List counting votes for each canidate
    candidate_list = [] #list of candidates
    percentage = [] #keeps percentage of votes per candidate
    answer = [] #store final answer

    for row in reader:
        candidate_list.append(row[2])
    
    totalVotes = len(candidate_list)

    for name in candidate_list:
        votesCount[name] += 1
    
    winner = max(zip(votesCount.values(),votesCount.keys()))
    names = tuple(votesCount.keys())
    votes = tuple(votesCount.values())

    for x in votes:
        percentage.append((int(x)/totalVotes)*100)
    answer.append('Election Results')
    answer.append('-----------------------')
    answer.append('Total Votes: ' + str(totalVotes))
    answer.append('-----------------------')
    for x in range(len(names)):
        answer.append(names[x] + ': ' + str(round(percentage[x],1)) + '% ' + '(' + str(votes[x]) + ')')
    answer.append('-----------------------')
    answer.append('Winner: ' + winner[1])
    answer.append('-----------------------')

    print("\n".join((answer)))

with open(newfile, 'w') as txtfile:
    txtfile.write('\n'.join(answer))

