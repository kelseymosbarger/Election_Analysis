# Election_Analysis
Module 3 - Python

## Overview of Election Audit
A colorado elections employee must analyze election data and answer the following prompts:
1. Calculate the total number of votes cast
2. Get a complete list of votes from each county
3. Calculate the total number of votes in each county
4. Calculate the percentage of votes among counties
5. Determine the county with the largest amount of votes
6. Get a complete list of candidates who recieved votes
7. Calculate the total number if votes each candidate recieved
8. Calculate the percentage of votes each candidate won
9. Determine the winner of election based on popular vote

## Resources
-Data Sources: election_results.csv (in resources folder)
-Software: Python 3.10, Visual Studio Code (not sure which version)

## Election Audit Results Summary
Election analysis results:
- There were 369,711 total votes cast in the election
- Votes were cast in three counties
  - Jefferson: 10.5% (38,855)
  - Denver 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
- There were 3 candidates that received votes:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The Candidate Results were:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election is Diana DeGette with 272,892 votes 73.8% of total votes

## Election-Audit Summary
- This code could be modified to be used for voting on ballot measures and issues as well as specific candidates by using binary instead of for loops, and calculating which result is greater than 50%.  Another way this code could be modified would be to add additional for loops which would to provide more voter data, such as demographics or political affiliation, to determine the political climate, assuming the .csv file can incorporate that information.  Finally, this code could be used to determine overall voter turnout by cross-referencing the total population with specific ballot IDs.

## Additional Information
- The challenge code PyPoll_Challenge.py is located in the resources folder
- The output election_analysis.txt is located in the analysis folder within the Resources folder

## Challenges
 - Github - issues with merging a branch which I don't understand because there is only one branch.  $ git push -f to force-push files into github, and five gray hairs later.
