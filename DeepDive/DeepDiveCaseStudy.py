'''
1. A Robot moves in a Plane starting from the origin point (0,0). The robot can move
toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given
following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after directions are steps. Write a program to compute the
distance current position after sequence of movements.
Hint: Use math module.
'''

import math

# Initialize the starting position
x = 0
y = 0

# List of movements
movements = [
    ('UP', 5),
    ('DOWN', 3),
    ('LEFT', 3),
    ('RIGHT', 2)
]

# Iterate over the movements
for direction, steps in movements:
    if direction == 'UP':
        y += steps
    elif direction == 'DOWN':
        y -= steps
    elif direction == 'LEFT':
        x -= steps
    elif direction == 'RIGHT':
        x += steps

# Calculate the distance from the origin
distance = math.sqrt(x**2 + y**2)

print("Distance from origin:", distance)

'''
2. Data of XYZ company is stored in sorted list. Write a program for searching
specific data from that list.
Hint: Use if/elif to deal with conditions.
'''

def search(data, target):
    # Binary search algorithm
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# Test the search function
data = [1, 3, 4, 6, 7, 8, 9, 11, 12, 14, 15]
target = 8
index = search(data, target)
if index >= 0:
    print("Target found at index", index)
else:
    print("Target not found")


'''
3. Weather forecasting organization wants to show is it day or night. So, write a
program for such organization to find whether is it dark outside or not.
Hint: Use time module.
'''

import time


def is_dark():
    # Get the current time
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Check if it is currently nighttime (between sunset and sunrise)
    sunset_hour = 18
    sunrise_hour = 6
    if sunset_hour <= hour < sunrise_hour:
        return True
    elif hour == sunrise_hour and minute == 0 and second == 0:
        return False
    elif hour == sunset_hour and minute == 0 and second == 0:
        return True
    else:
        return False


# Test the is_dark function
if is_dark():
    print("It is dark outside.")
else:
    print("It is not dark outside.")

'''
4. Write a program to find distance between two locations when their latitude and
longitudes are given.
Hint: Use math module.
'''

#import math

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Calculate the differences
    lat_diff = lat2 - lat1
    lon_diff = lon2 - lon1

    # Calculate the distance using the haversine formula
    a = math.sin(lat_diff / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(lon_diff / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Return the distance in kilometers
    return 6371 * c

# Test the function with the coordinates of two locations
lat1 = 52.3296788
lon1 = 21.0122387
lat2 = 51.5077509
lon2 = -0.1497583

distance = haversine(lat1, lon1, lat2, lon2)
print(f"The distance between the two locations is {distance:.2f} kilometers.")

'''
5. Design a software for bank system. There should be options like cash withdraw,
cash credit and change password. According to user input, the software should
provide required output.
Hint: Use if else statements and functions.
'''

def main():
    # Print the menu
    print("1. Cash withdrawal")
    print("2. Cash credit")
    print("3. Change password")
    print("4. Exit")

    # Get the user's choice
    choice = int(input("Enter your choice: "))

    # Handle the user's choice
    if choice == 1:
        cash_withdrawal()
    elif choice == 2:
        cash_credit()
    elif choice == 3:
        change_password()
    elif choice == 4:
        exit()
    else:
        print("Invalid choice.")

def cash_withdrawal():
    # Get the amount to withdraw
    global balance
    amount = int(input("Enter the amount to withdraw: "))

    # Check if the user has sufficient balance
    if balance < amount:
        print("Insufficient balance.")
    else:
        # Update the balance and print the new balance
        balance -= amount
        print(f"Your new balance is {balance}.")

def cash_credit():
    # Get the amount to credit
    amount = int(input("Enter the amount to credit: "))

    # Update the balance and print the new balance
    global balance
    balance += amount
    print(f"Your new balance is {balance}.")

def change_password(current_password=1234):
    # Get the current password
    password = input("Enter your current password: ")

    # Check if the password is correct
    if password != current_password:
        print("Incorrect password.")
    else:
        # Get the new password
        new_password = input("Enter your new password: ")

        # Update the password
        current_password
        current_password = new_password
        print("Password changed successfully.")

balance = 1000
current_password = "password"

# Run the main program loop
while True:
    main()


#6. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtainedshould be printed in a comma-separated sequence on a single line.


result = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        result.append(str(i))

print(','.join(result))



'''
7. Write a program which can compute the factorial of a given numbers. Use recursion
to find it.
Hint: Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''

def factorial(n):
    # Base case: the factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: the factorial of n is n * the factorial of n-1
    else:
        return n * factorial(n-1)

# Test the function with the number 8
result = factorial(8)
print(result)



'''
8. Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H: C is 50. H is 30.
D is the variable whose values should be input to your program in a commaseparated sequence.
 Example:
Let us assume the following comma separated input sequence is given to the
program:
100,150,180
The output of the program should be:
18,22,24
'''

import math

# Fixed values of C and H
C = 50
H = 30

# Get the input sequence of values for D
D_str = input("Enter a comma-separated sequence of values for D: ")

# Split the input string into a list of values for D
D_list = [int(x) for x in D_str.split(",")]

# Calculate and print the value of Q for each value of D
for D in D_list:
    Q = math.sqrt(2 * C * D / H)
    print(f"Q = {Q:.2f}")


'''
9. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional
array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡-Y-1.
Example:
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
'''

# Get the input values for X and Y
x = int(input("Enter a value for X: "))
y = int(input("Enter a value for Y: "))

# Initialize the 2-dimensional array with zeros
array = [[0] * y for i in range(x)]

# Loop through the rows and columns of the array
for i in range(x):
    for j in range(y):
        # Set the element value to i * j
        array[i][j] = i * j

# Print the array
print(array)


'''
10.Write a program that accepts a comma separated sequence of words as input and
prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
 without,hello,bag,world
 Then, the output should be:
 bag,hello,without,world
'''

# Get the input sequence of words
words_str = input("Enter a comma-separated sequence of words: ")

# Split the input string into a list of words
words = [x for x in words_str.split(",")]

# Sort the words alphabetically
words.sort()

# Print the sorted words as a comma-separated sequence
print(", ".join(words))


'''
11.Write a program that accepts sequence of lines as input and prints the lines after
making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
 Hello world
 Practice makes perfect
 Then, the output should be:
 HELLO WORLD
 PRACTICE MAKES PERFECT
'''

def capitalizer(lines):
    # Convert each line to uppercase
    lines = [line.upper() for line in lines]

    # Return the capitalized lines as a list
    return lines

# Test the function with some example input
print(capitalizer(['Hello world', 'Practice makes perfect']))



'''
12.Write a program that accepts a sequence of whitespace separated words as input
and prints the words after removing all duplicate words and sorting them
alphanumerically.
Suppose the following input is supplied to the program:
 hello world and practice makes perfect and hello world again
 Then, the output should be:
 again and hello makes perfect practice world
'''

def deduplicate_and_sort(words):
    # Split the input string into a list of words
    words = words.split()

    # Remove duplicates and sort the list
    words = sorted(set(words))

    # Return the deduplicated and sorted list as a string
    return ' '.join(words)

# Test the function with some example input
print(deduplicate_and_sort('hello world and practice makes perfect and hello world again'))



'''
13.Write a program which accepts a sequence of comma separated 4 digit binary
numbers as its input and then check whether they are divisible by 5 or not. The
numbers that are divisible by 5 are to be printed in a comma separated sequence.
Module 3 – Deep Dive - Functions, OOPs, Modules, Errors and Exceptions

Example:
0100,0011,1010,1001
Then the output should be:
1010
'''

def divisible_by_5(numbers):
    # Split the input string into a list of numbers
    numbers = numbers.split(',')

    # Convert each number to an integer
    numbers = [int(number, 2) for number in numbers]

    # Keep only the numbers that are divisible by 5
    numbers = [number for number in numbers if number % 5 == 0]

    # Convert the numbers back to binary strings
    numbers = [bin(number)[2:] for number in numbers]

    # Return the numbers as a comma-separated string
    return ','.join(numbers)

# Test the function with some example input
print(divisible_by_5('0100,0011,1010,1001'))



'''
14.Write a program that accepts a sentence and calculate the number of upper case
letters and lower case letters.
 Suppose the following input is supplied to the program:
 Hello world!
 Then, the output should be:
 UPPER CASE 1
 LOWER CASE 9
'''


def count_case(sentence):
    # Initialize counters for upper and lower case letters
    upper = 0
    lower = 0

    # Iterate over the characters in the sentence
    for c in sentence:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1

    # Return the counts as a dictionary
    return {'UPPER CASE': upper, 'LOWER CASE': lower}

# Test the function with some example input
print(count_case('Hello world!'))


'''
15. Give example of fsum and sum function of math library.
'''


import math

# Use the fsum function to calculate the sum of a list of floats
numbers = [0.4, 0.3, 0.7, 0.4]
result = math.fsum(numbers)
print(result)  # Output: 1.0

# Use the sum function to calculate the sum of a list of integers
numbers = [5, 7, 8, 11]
result = sum(numbers)
print(result)  # Output: 10

# Use the sum function to calculate the sum of a list of mixed types
numbers = [12, 22.5, 30, 44.5]
result = sum(numbers)
print(result)  # Output: 11.0
