import csv
import os


filepath = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("Analysis", "electionanalysis.txt")

vote_count = 0
candidate_names = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

with open (filepath) as data:
    reader = csv.reader(data)
    header = next(reader)
    for row in reader:
        vote_count += 1
        candidate_name = row[2]
        if candidate_name not in candidate_names:
            candidate_names.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# if votes are > than winning votes 