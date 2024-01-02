import csv
import os
 
# csv file name
csv_file = os.path.join("Resources", "election_data.csv")

# result file name
text_file = os.path.join("analysis", "PyPoll_Result.txt")

# variable to store header row
fields = []

# variables for output
vote_total = 0
curr_candidate = ''
curr_vote = 0
curr_vote_pct = 0
cand_list = []
cand_vote = {}
max_vote = 0
max_vote_cand = ''
tie_flag = 'N'

# reading csv file
with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # extracting headers through first row
    fields = next(csvreader)
     
    # extracting each data row one by one
    for row in csvreader:
        vote_total = vote_total + 1
        #print("Current Record: {}, {}, {}, {}".format(vote_total, row[0], row[1], row[2]))
        curr_candidate = row[2]
        if curr_candidate not in cand_list:
            cand_list.append(curr_candidate)
            cand_vote[curr_candidate] = 0
        cand_vote[curr_candidate] = cand_vote[curr_candidate] + 1

with open(text_file, "w") as textfile:
    print("Election Results")
    print("----------------------------")
    print("Total Votes: {}".format(vote_total))

    print("Election Results", file=textfile)
    print("----------------------------", file=textfile)
    print("Total Votes: {}".format(vote_total), file=textfile)    

    for cand in cand_vote:
        curr_vote = cand_vote.get(cand)
        curr_vote_pct = round(curr_vote / vote_total, 5) * 100
        if curr_vote == max_vote:
            max_vote_cand = max_vote_cand + ', ' + cand
            tie_flag = 'Y'
        if curr_vote > max_vote:
            max_vote = curr_vote
            max_vote_cand = cand
            tie_flag = 'N'

        print("{}: {}% ({})".format(cand, curr_vote_pct, curr_vote))
        print("{}: {}% ({})".format(cand, curr_vote_pct, curr_vote), file=textfile)

    if tie_flag == 'Y':
        print("------There is a tie--------")
        print("------There is a tie--------", file=textfile)

    print("----------------------------")
    print("Winner: {}".format(max_vote_cand))
    print("----------------------------")
    
    print("----------------------------", file=textfile)
    print("Winner: {}".format(max_vote_cand), file=textfile)
    print("----------------------------", file=textfile)
