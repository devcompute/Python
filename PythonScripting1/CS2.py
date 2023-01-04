'''
A code that accepts a sequence of words as inputs and prints them in alphabetical order.
'''

# Get the user's input
words = input("Enter a sequence of words: ")

# Split the input string into a list of words
word_list = words.split()

# Sort the list of words
sorted_words = sorted(word_list)

# Print the sorted list of words
print(sorted_words)
