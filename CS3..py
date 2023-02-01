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
