## PyPoll:

import os
import csv
# set path for files:
election_data = os.path.join ('..\PyPoll', 'election_data.csv')

#Set variables:
#Text file
text_path = 'election_analysis.txt'
election_analysis = os.path.join('analysis', 'election_analysis.txt')

# Total votes
total_votes = 0

# List of candidates
candidate_names = []

# percentage of votes & total number of votes each candidate won
candidate_votes_received = {}
percentage_candidate_votes_received = {}

# winner of the election based on popular vote
winning_candidate = ""
winning_candidate_vote_count = 0
winning_candidate_percentage = 0

with open(election_data) as election_data:
     new_var = open('election_data.csv')
     with new_var as csvfile:
        file_reader = csv.reader(election_data)
csvreader = csv.reader(csvfile)
csv_header2 = next(file_reader)
for row in file_reader:

     total_votes += 1

# candidate names
candidate_name = row[2]

# candidate names added to list
if candidate_name not in candidate_names:
     candidate_names.append(candidate_name)

# candidate votes being counted
candidate_votes_received[candidate_name] = 0
candidate_votes_received[candidate_name] += 1

# Add results to text file
with open(election_analysis, 'w') as txt_file:
# Final vote count printed:
     election_results = (
        f'\nElection Results\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-------------------------\n')
print(election_results, end ='')

txt_file.write(election_results)
for candidate in candidate_votes_received:

# vote count & percentage of votes
    votes = candidate_votes_received[candidate]
    vote_percentage = float(votes) / float(total_votes) * 100
candidate_results = (
     f'{candidate}: {vote_percentage:.1f}% ({votes:,})\n')

print(candidate_results)

# Add to text file
txt_file.write(candidate_results)

# Final result calculations
if (votes > winning_candidate_vote_count) and (vote_percentage > winning_candidate_percentage):
     winning_candidate_vote_count = votes
     winning_candidate = candidate
     winning_candidate_percentage = vote_percentage

# Print final Results
winning_candidate_results = (
     f'-------------------------\n'
     f'Winner: {winning_candidate}\n'
     f'Winning Candidate Vote Count: {winning_candidate_vote_count:,}\n'
     f'Winning Candidate Percentage: {winning_candidate_percentage:1f}%\n'
     f'-------------------------\n'
)
print(winning_candidate_results)

# Final text file addition
txt_file.write(winning_candidate_results)