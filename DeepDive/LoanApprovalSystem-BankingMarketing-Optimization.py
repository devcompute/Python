'''

Business challenge/requirement
Bank of Portugal runs marketing campaign to offer loans to clients. Loan is offered to
only clients with particular professions. List of successful campaigns (with client
data) is given in attached dataset. You have to come up with program which reads
the file and builds a set of unique profession list and given input profession of client –
system tells whether client is eligible to be approached for marketing campaign.

Key issues
Tele Caller can only make x number of cold calls in a day. Hence to increase her
effectiveness only eligible customers should be called

Considerations
Current system does not differentiate clients based on age and profession

Data volume
447 records in bank-data.csv
Additional information
- NA

Business benefits
Company can achieve between 15% to 20% higher conversion by targeting right
clients.

Approach to Solve
You have to use fundamentals of Python taught in module 3
1. Read file bank-data.csv
2. Build a set of unique jobs
3. Read the input from command line –profession
4. Check if profession is in list
5. Print whether client is eligible

Enhancements for code
You can try these enhancements in code
1. Compute max and min age for loan eligibility based on data in csv file
2. Store max and min age in dictionary
3. Make the profession check case insensitive
4. Currently program ends after the check. Take the input in while loop and end
only if user types "END" for profession
'''

import csv


def get_professions_and_ages():
    # Initialize an empty set to store the professions
    professions = set()

    # Initialize dictionaries to store the minimum and maximum ages
    min_ages = {}
    max_ages = {}

    # Open the CSV file and read the professions and ages
    with open('bank-data.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            profession = row['profession']
            age = int(row['age'])
            professions.add(profession)

            # Update the minimum and maximum ages for this profession
            if profession in min_ages:
                min_ages[profession] = min(min_ages[profession], age)
                max_ages[profession] = max(max_ages[profession], age)
            else:
                min_ages[profession] = age
                max_ages[profession] = age

    # Return the set of professions and the dictionaries of ages
    return professions, min_ages, max_ages


def is_eligible(profession, professions, min_ages, max_ages, age):
    # Convert the profession to lowercase to make the check case-insensitive
    profession = profession.lower()

    # Check if the profession is in the set of professions
    if profession in professions:
        # Check if the age is within the minimum and maximum ages for this profession
        if age >= min_ages[profession] and age <= max_ages[profession]:
            return True
        else:
            return False
    else:
        return False


# Read the professions and ages from the CSV file

# Run a loop to allow the user to input multiple professions
while True:
    # Get the input from the user
    profession = input('Enter a profession (or "END" to exit): ')

    # Check if the user wants to exit the loop
    if profession.lower() == 'end':
        break

    # Get the age from the user
    age = int(input('Enter the age: '))

#This Python program will define the functions of 'get_professions()' and 'is_eligible()' for determining the persons professional and based on that profession if they qualify for the loan.
#The 'get_professions()" reads professions from 'bank-data.csv' file and returns sets of unique professions.
#The 'is_eligible()' function takes the professions as sets as inputs and return true or false for the parameters.
#Also, code is added to compute max/min age for loan eligibility based on CSV files to store in dictionary.
#An while loop is added to able the user to input multiple professions to check eligibility.
