# Data that will need to be retrieved:
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of the election based on popular vote

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Assign a variable for the file to load and the path. (direct method)
#file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # To do: perform analysis.
    #print(election_data)

# Assign a variable for the file to load and the path. (INDIRECT method)
#import csv
#import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
     #print(election_data)

# Dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initializing total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
candidate_votes = {}
# Winning candidate & winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to total vote count.
        total_votes += 1
        # Printing candidate name from each row.
        candidate_name = row[2]
        # If the candidate doesn't match any existing candidate
        if candidate_name not in candidate_options:
            # Adding to list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that the candidate's votes count.
            candidate_votes[candidate_name] = 0
        # Adding vote to the candidate's count.
        candidate_votes[candidate_name] += 1

# Saving results to text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    # Determining % of votes for each candidate by looping through the counts.
    # Iterating through candidate list
    for candidate_name in candidate_votes:
        # Retreive vote count of a candidate.
        votes =  candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candiate's voter count & % to terminal
        print(candidate_results)
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate.
        # Determine if votes are greater than the winning count.
    if(votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count = votes
        winning_percentage = candidate_name
        winning_candidate = vote_percentage
    # Print winning candidate's results to terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
txt_file.write(winning_candidate_summary)