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

# this is to create the first part of the summary (total votes)
with open (output_file, "w") as text_file:
    output = (f"""
    Election Results
    ----------------------------
    Total Votes: {vote_count}
    """)

    print(output)

    # write the output to the text file
    text_file.write(output)

    # this will track each candidate's votes
    for candidate_name in candidate_votes:
        # each time the candidate is logged, the votes will be added to their total
        votes = candidate_votes.get(candidate_name)
        # calculates the percentage
        vote_percentage = float(votes) / float(vote_count) * 100

        # if the votes for that candidate are greater than the current count, they have the winning vote
        if (votes > winning_count):

            # that number is now the winning vote along with the matching candidate
            winning_count = votes
            winning_candidate = candidate_name
        
        # the voter infomration will be written to the text file in this format
        vote_output = (f"""
        {candidate_name}: {vote_percentage:.3f}% ({votes})
        """)

        print(vote_output)

        text_file.write(vote_output)


    winner_output = (
        f"""
        -------------------------
        Winner: {winning_candidate}
        -------------------------
        """)

    print(winner_output)

    text_file.write(winner_output)





