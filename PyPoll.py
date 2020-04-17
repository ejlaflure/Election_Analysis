#Add dependencies to open data file.
import os
import csv
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate Options and Candidate Votes
candidate_options = []
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Read each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Find the candidate names from each row.
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate, add the candidate list.
        if candidate_name not in candidate_options:
           # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
           # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Write data we need to retrieve to our text file.
with open(file_to_save, "w") as txt_file:
    #Total number of votes cast
    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
    txt_file.write(election_results)
    
    # Retrieve vote count and percentage for each candidate.
    for candidate in candidate_votes:
        # Vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        #Write the candidate list to text file.
        txt_file.write(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Winning vote count and candidate.
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent = vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # Set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate
    
    #Write the winner of the election based on popular vote to text file.
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    txt_file.write(winning_candidate_summary)