"""
Business challenge/requirement
You are a data analyst with University of Cal USA (Not a machine learning expert yet
as you still have not completed ML with Python Course :-)).The University has data of
Math, Physics and Data Structure score of sophomore students. This data is stored in
different files. The University has hired a data science company to do analysis of
scores and find if there is any correlation of score with age, ethnicity etc. Before the
data is given to the company you have to do data wrangling.

Key issues
Ensure students identify is not revealed to the agency and only relevant data is
shared

Considerations
NONE

Data volume
- In thousands, but only around 1800 records are shared in files MathScoreTerm1.csv
DSScoreTerm1.csv, PhysicsScoreTerm1.csv

Additional information
- NA

Business benefits
University can get more students enrollment by improving its international ranking
through personalized course/curriculum for students

Approach to Solve
You have to use fundamentals of Numpy and Pandas covered in module 4.
    1. Read the three csv files which contains the score of same students in term1 for
    each Subject
    2. Remove the name and ethnicity column (to ensure confidentiality)
    3. Fill missing score data with zero
    4. Merge the three files
    5. Change Sex(M/F) Column to 1/2 for further analysis
    6. Store the data in new file – ScoreFinal.csv

Enhancements for code
You can try these enhancements in code
    1. Convert ethnicity to numerical value
    2. Fill the missing score for a student to the average of the class
"""

import pandas as pd

# Read the score data for each subject in a DataFrame
math_scores = pd.read_csv("MathScoreTerm1.csv")
ds_scores = pd.read_csv("DSScoreTerm1.csv")
physics_scores = pd.read_csv("PhysicsScoreTerm1.csv")

# Drop the 'name' and 'ethnicity' columns from each DataFrame
math_scores = math_scores.drop(columns=["name", "ethnicity"])
ds_scores = ds_scores.drop(columns=["name", "ethnicity"])
physics_scores = physics_scores.drop(columns=["name", "ethnicity"])

# Fill missing score data with zero
math_scores.fillna(0, inplace=True)
ds_scores.fillna(0, inplace=True)
physics_scores.fillna(0, inplace=True)

# Merge the DataFrames on the 'id' column
scores = pd.merge(math_scores, ds_scores, on="id")
scores = pd.merge(scores, physics_scores, on="id")

# Map 'M' and 'F' to 1 and 2 in the 'sex' column
scores['sex'] = scores['sex'].map({'M': 1, 'F': 2})

# Write the DataFrame to a CSV file
scores.to_csv("ScoreFinal.csv", index=False)
