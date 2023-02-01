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

