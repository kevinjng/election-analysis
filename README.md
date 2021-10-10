# Election Analysis

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.7, Visual Studio Code 1.60.2

## Audit Overview
The following audit reviews a recent congressional election's results between three candidates from three different counties. The three candidates running for the congressional seat are Mr. Charles Stockham, Ms. Diana DeGette, and Mr. Raymon Doane with results taken from the Jefferson, Denver, and Arapahoe counties.

The following results are analyzed to produce the voter turnout for each respective county, the percentage of votes per county out of the entire count, and which county had the highest voter turnout.

## Election Audit Results
<INSERT IMAGE>
- There was a total of **369,711 votes** casted in this congressional election.
- Out of the 369,711 votes casted, **82.8% of the votes** were received in Denver County, **10.5% (38,855)** in Jefferson County, and **6.7% (24,801)** in Arapahoe County.
- **Denver County represents the largest portion of the total votes** with 306,055 votes placed within this precinct.
- Ms. Diana DeGette received **73.8% of the total votes**, Mr. Charles Stockham received **23% (85,213)**, and finally Mr. Raymon Doane with **3.1% (11,606)**.
- **Ms. Diana DeGette obtains the congressional seat with 272,892 votes** which almost makes up three-quarters of the total votes casted in the election.

## Election Audit Summary
One way the Python script can be modified is by taking this analysis a step further to review which votes came from which county for a specific candidate. This would require script that counts each row and takes the candidate being voted for, and which county the vote originated from, to determine how many votes a single candidate received from a specific county. The results extracted from this particular analysis would show how popular a candidate is within a county and if a candidate received a majority of votes from a particular county.

This same methodology could be applied to other elections on a much larger scale, such as state governor elections, which would be most beneficial for states with numerous counties, such as Texas, Georgia, and Virginia. Or, with presidential elections which would take total votes casted within the fifty states containing the 3,000+ counties in the United States.

If there were some further basic information provided, such as total number of registered voters per county or age of voters that casted votes for example, the script could be modified to add further depth to an election analysis.

If the total number of registered voters were provided, one could determine the participating voter turnout in a particular county which would measure voter activity within the county for an election. For this scenario, the total amount of registered voters would most likely need to be given as a set value obtained from official census data and utilized as a variable within the script. Then, the script would need to divide the voter turnout within a given election by the registered voter amount to determine the voter activity for a specific county.

Now if the age of voters that casted votes were provided, this would present a valuable demographic analysis for a given election showing which candidates are popular within a certain age group. If this were the case, a similar dataset like *election_results.csv* would need to be used, but the age of a voter would need to be requested from the voter and inputted into another column on the dataset. With this modified dataset, the script could be modified to count each row and track each voter's age, and combine it with the candidate they chose, to determine popular age groups for specific candidates. Furthermore, a maximum and minimum portion of script could be utilized to help construct the age groups for the candidate, which would show if a candidate were more popular within younger, middle-aged, or elderly populations.

In conclusion, the script constructed and utilized for this election can be modified in various ways to provide a deeper analysis for any type of election whether new variables are given, or if the existing script is reoriented to compare already existing values to produce a broader analysis.