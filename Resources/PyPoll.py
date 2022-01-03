# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes eac candidate won
# 5. the winner of the elcetion based on popular vote

# Import the datetime class from the datetime module.
#import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is", now)

# Add dependancies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)












# Close the file
##election_data.close()

# Create a filename variable to a direct or indirect path to the file
##import os
##file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a test file
#with open(file_to_save, "w") as txt_file:

    # Write three counties to the file
    #txt_file.write("Arapahoe")
    #txt_file.write("Denver")
    #txt_file.write("Jefferson")
    #txt_file.write("Arapahoe, Denver, Jefferson")
    #txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")


# Close the File
#outfile.close()
