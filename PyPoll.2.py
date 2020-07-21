# Dependencies
import csv

# Files
file_load = "election_data.csv"
file_output = "election_analysis.txt"

# Total
total_votes = 0

# Candidate Options and Vote Counters
can_options = []
can_votes = {}

# Winner info
win_can = ""
win_count = 0

# Read the csv and convert it into a list of dictionaries
with open(file_load) as data:
    reader = csv.DictReader(data)

    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # get the name from each row
        can_name = row["Candidate"]

        # If the candidate is not already in list
        if can_name not in can_options:

            # Add it to the list
            can_options.append(can_name)

            # begin tracking their voter count
            can_votes[can_name] = 0

        # add a vote to their count
        can_votes[can_name] = can_votes[can_name] + 1

# Print and export
with open(file_output, "w") as txt_file:

    # terminal print - total votes
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results)

    # write total to txt file
    txt_file.write(election_results)

    # pick winner
    for candidate in can_votes:

        # get vote count and percentage
        votes = can_votes.get(candidate)
        vote_per = float(votes) / float(total_votes) * 100

        if (votes > win_count):
            win_count = votes
            win_can = candidate

        # terminal print - all can voter count and percentage
        voter_output = f"{candidate}: {vote_per:.3f}% ({votes})\n"
        print(voter_output)

        # all vote info to txt file
        txt_file.write(voter_output)

    # terminal print-winner
    win_can_output = (
        f"-------------------------\n"
        f"Winner: {win_can}\n"
        f"-------------------------\n")
    print(win_can_output)

    # winners name to txt file
    txt_file.write(win_can_output)
