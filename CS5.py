# Get the user's input
number = input("Enter a number: ")

# Reverse the number and store it in a new variable
reversed_number = number[::-1]

# Compare the original number to the reversed number
if number == reversed_number:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

