

import csv
import os
from operator import itemgetter

#   refenence file
csvpath = os.path.join(r"C:\Users\Kels\AppData\Local\Temp\Temp2_Starter_Code (1).zip\Starter_Code\PyPoll\Resources\election_data.csv")

#   variables
votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}

#   Open csv file
with open(csvpath) as election_data:
    reader = csv.DictReader(election_data)

    #   Create loop to process the data
    for row in reader:
        votes += 1
        candidate = row["Candidate"]

        if candidate not in candidate_options:
            candidate_options.append(candidate)
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] += 1

        if candidate_votes[candidate] > greatest_votes[1]:
            greatest_votes = [candidate, candidate_votes[candidate]]

#   Print in terminal
print()
print()
print()
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(votes))
print("-------------------------")

#   Print results for each candidate
for candidate in candidate_votes:
    percentage = round((candidate_votes[candidate] / votes) * 100, 2)
    print(f"{candidate}: {percentage}% ({candidate_votes[candidate]})")

print("-------------------------")
print("Winner: " + greatest_votes[0])
print("-------------------------")

#   Output file path
output_path = "output.txt"

#   Write results as a text file
with open(output_path, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Total Votes: " + str(votes) + "\n")
    txt_file.write("-------------------------\n")
    for candidate in candidate_votes:
        percentage = round((candidate_votes[candidate] / votes) * 100, 2)
        txt_file.write(f"{candidate}: {percentage}% ({candidate_votes[candidate]})\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Winner: " + greatest_votes[0] + "\n")
    txt_file.write("-------------------------\n")

