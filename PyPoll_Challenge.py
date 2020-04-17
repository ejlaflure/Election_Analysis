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
# County Options and County Votes
county_options = []
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Largest County Tracker
largest_county = ""

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
        # Find the county names from each row.
        county_name = row[1]
        
        # If the candidate does not match any existing candidate, add to the candidate list.
        if candidate_name not in candidate_options:
           # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
           # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # If the county does not match any existing counties, add to the county list.
        if county_name not in county_options:
           # Add the county name to the county list.
            county_options.append(county_name)
           # Begin tracking that county's vote count. 
            county_votes[county_name] = 0
        # Add a vote to that county's count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Retrieve vote count and percentage for each county.
    for county in county_votes:
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each county's voter count and percentage to the terminal.
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        # Save the county list to text file.
        txt_file.write(county_results)

        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent = vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # Set the largest_county equal to the county's name.
         largest_county = county
 
    # Print the largest county contributer to terminal.
    largest_county_turnout = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(largest_county_turnout)
    # Save the largest county contributer to the text file.
    txt_file.write(largest_county_turnout)

    # Reset Winning Count Tracker
    winning_count = 0
    winning_percentage = 0

    # Retrieve vote count and percentage for each candidate.
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate's voter count and percentage to the terminal.
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent = vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # Set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate
    
    #Print the winner of the election based on popular vote to terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)