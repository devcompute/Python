#QUESTION 1


def find_factors(number):
    # Create an empty list to store the factors
    factors = []
    # Loop through the range from 1 to the number
    for i in range(1, number+1):
        # If the number is evenly divisible by i, it is a factor
        if number % i == 0:
            factors.append(i)
    return factors

# Get the user's input
number = int(input("Enter a number: "))

# Find the factors of the number
factors = find_factors(number)

# Print the factors and whether they are even or odd
for factor in factors:
    if factor % 2 == 0:
        print(f"{factor} is even")
    else:
        print(f"{factor} is odd")


#QUESTION 2



# Get the user's input
words = input("Enter a sequence of words: ")

# Split the input string into a list of words
word_list = words.split()

# Sort the list of words
sorted_words = sorted(word_list)

# Print the sorted list of words
print(sorted_words)



#QUESTION 3


# Initialize an empty list to store the numbers
numbers = []

# Loop through the range from 1000 to 3001
for i in range(1000, 3001):
    # Convert the number to a string
    number_str = str(i)
    # Initialize a flag to track whether all digits are even
    all_even = True
    # Loop through each character in the number
    for ch in number_str:
        # If the character is not an even digit, set the flag to False
        if int(ch) % 2 != 0:
            all_even = False
            break
    # If the flag is still True, the number has all even digits
    if all_even:
        numbers.append(i)

# Join the numbers in the list with a comma and print the result
print(", ".join(str(n) for n in numbers))




#QUESTION 4


# Get the user's input
sentence = input("Enter a sentence: ")

# Initialize counters for the number of letters and digits
letter_count = 0
digit_count = 0

# Loop through each character in the sentence
for ch in sentence:
    # If the character is a letter, increment the letter count
    if ch.isalpha():
        letter_count += 1
    # If the character is a digit, increment the digit count
    elif ch.isdigit():
        digit_count += 1

# Print the results
print(f"Number of letters: {letter_count}")
print(f"Number of digits: {digit_count}")





#QUESTION 5


# Get the user's input
number = input("Enter a number: ")

# Reverse the number and store it in a new variable
reversed_number = number[::-1]

# Compare the original number to the reversed number
if number == reversed_number:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")


