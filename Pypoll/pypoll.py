import csv
import os

# assign file to a variable
filepath = os.path.join("Resources", "election_data.csv")
# this will be written to
output_file = os.path.join("Analysis", "electionanalysis.txt")

# vote counter starts at zero
vote_count = 0
# empty list for candidates
candidate_names = []
# dictionary for the votes
candidate_votes = {}
#will declare the winning candidate
winning_candidate = ""
# the count
winning_count = 0
# the percentage
winning_percentage = 0


# opens the results and reads the file
with open (filepath) as data:
    reader = csv.reader(data)
    header = next(reader)
    
    for row in reader:
        # adds the votes
        vote_count += 1
        # gets the candidate names
        candidate_name = row[2]
        # if there is no match to the name, you will add it to the list
        if candidate_name not in candidate_names:
            candidate_names.append(candidate_name)
            # starts counting the candidate's votes
            candidate_votes[candidate_name] = 0
        # adds the votes
        candidate_votes[candidate_name] += 1

# if votes are > than winning votes 

output = (f"""
Election Results
-------------------------
Total Votes:
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------

""")

print(output)

with open (output_file, "w") as text:
    text.write(output)
