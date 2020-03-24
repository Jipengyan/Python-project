import os
import csv
PyPollcsv=os.path.join("/Users/jyan0/UCBwork/Python-project/Instructions/PyPoll/Resources/election_data.csv")
total_votes=[]
candidates_list=[]
single_candidate=[]
vote_percent_won=[]
vote_number_won=[]
winner=[]
count=0
with open(PyPollcsv, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
    for row in csvreader:
        count=count+1
        candidates_list.append(row[2])
    for a in set(candidates_list):
        single_candidate.append(a)
        b=candidates_list.count(a)
        vote_number_won.append(b)
        c=(b/count)*100
        vote_percent_won.append(c)
    winner_vote_number_won=max(vote_number_won)
    winner=single_candidate[vote_number_won.index(winner_vote_number_won)]
print("Total votes:"+str(count))
for i in range(len(single_candidate)):
        print(single_candidate[i]+":"+str(vote_percent_won[i])+"%("+str(vote_number_won[i])+")")
print("The winner is:"+winner) 


