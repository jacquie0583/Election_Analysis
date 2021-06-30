# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os
# Add a variable to load a file from a path.
file_to_load = os.path.join(r"C:\Users\jacqu\Desktop\Class Folder\Election_Analysis","election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join(r"C:\Users\jacqu\Desktop\Class Folder\Election_Analysis","election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options list and candidate votes dictionary.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary. #  Initialize a dictionary that will hold the county as the key and the votes cast for each county as the values.
county_list = []
county_votes = {}
 # Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# 2: Track the largest county voter turnout and its percentage
largest_turnout_count = 0
largest_turnout_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Loop each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes = total_votes +  1
        # 3: Extract the county name from each row.
        candidate_name = row[2]
        # Get the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate, add the candidate list.
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1


    # 4a: Write an if statement that checks that the county does not match any existing county in the county list. If the county does not match any existing county add it to he county list
        if county_name not in county_list:
    # 4b:  Add the county name to the county list.
           county_list.append(county_name)
    # 4c: Begin tracking the county's vote count.
           county_votes[county_name] = 0

    # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")
    print(election_results, end="")    
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # 6a: Write a for loop to save final county vote count to text file, get the county from the county dictionary.
    for county_name in county_list:
    # 6b: Retrieve the county vote count.
        all_votes = county_votes[county_name]
    # 6c: Calculate the percentage of votes for the county.
        all_votes_percentage = (float(all_votes)/float(total_votes)) * 100  
    # 6d: Print the county results to the terminal. Print each county's voter count and percentage to the terminal.
        county_results = (f"{county_name}: {all_votes_percentage:.1f}% ({all_votes:,})\n")
        print (county_results)
    # 6e: Save the county votes to a text file.  
        txt_file.write(county_results)

    # 6f: Write an if statement to determine the winning county and get its vote count.
        if (all_votes > largest_turnout_count) and (all_votes_percentage > largest_turnout_percentage):
                largest_turnout_count = all_votes
                largest_turnout_percentage = all_votes_percentage
                largest_turnout_county = county_name
    txt_file.write("n")

     
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout:   {largest_turnout_county}\n"
        f"-------------------------\n")         
     # 7: Print the county with the largest turnout to the terminal. Print the winning county (to terminal)
    print(winning_county_summary)
     

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

 # Save the final candidate results to the text file.
    for candidate in candidate_options:
        # Retrieve vote count and percentage.
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)/float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
        )

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        txt_file.write(candidate_results)


# Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n"
    )
    print(winning_candidate_summary)

# Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
