import csv
import os

file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join('analysis', 'election_results.txt')


total_votes = 0

candidates = []
candidate_votes = {}
winning_candidate = ''
winning_candidate_count = 0
winning_candidate_percentage = 0

counties = []
county_votes = {}
winning_county = ''
winning_county_count = 0


with open(file_to_load, 'r') as electon_data:
    
    file_reader = csv.reader(electon_data)

    headers = next(file_reader)

    for row in file_reader:

        total_votes += 1

        candidate_name = row[2]
        county_name = row[1]

        if county_name not in counties:

            counties.append(county_name)

            county_votes[county_name] = 0

        county_votes[county_name] += 1

        if candidate_name not in candidates:

            candidates.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1


    with open(file_to_save, 'w') as txt_file:

        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n"
            )
        print(election_results)
        # Save the final vote count to the text file.
        txt_file.write(election_results)




        print("County Votes:")
        txt_file.write("\nCounty Votes:\n")

        for county in counties:

            votes = county_votes[county]

            vote_percentage = float(votes) / float(total_votes) * 100

            county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})")

            print(county_results)
            txt_file.write(f"{county_results}\n")

            if votes > winning_county_count:

                winning_county_count = votes

                winning_county = county


        winning_county_summary = (
            f"\n-------------------------\n"
            f"Largest County Turnout: {winning_county}\n"
            f"-------------------------\n"
        )

        print(winning_county_summary)
        txt_file.write(winning_county_summary)



        for candidate in candidates:

            votes = candidate_votes[candidate]

            vote_percentage = float(votes) / float(total_votes) * 100

            candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

            print(candidate_results)
            txt_file.write(candidate_results)


            if votes > winning_candidate_count:

                winning_candidate_count = votes

                winning_candidate = candidate

                winning_candidate_percentage = vote_percentage


        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_candidate_count:,}\n"
            f"Winning Percentage: {winning_candidate_percentage:.1f}%\n"
            f"-------------------------"
        )

        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)

        