import csv


def get_professions_and_ages():
    # Initialize an empty set to store the professions
    professions = set()

    # Initialize dictionaries to store the minimum and maximum ages
    min_ages = {}
    max_ages = {}

    # Open the CSV file and read the professions and ages
    with open('/Users/benjaminadams/Downloads/777_m3_datasets_v1.0/bank-data.csv', 'r') as f:
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