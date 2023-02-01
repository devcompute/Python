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
