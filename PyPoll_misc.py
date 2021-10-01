# Dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

    # Writing data to file.
    txt_file.write("Counties in the Election")
    txt_file.write("\n-------------------------")

    # Write 3 counties to the file.
    txt_file.write("\nArapahoe \nDenver \nJefferson")