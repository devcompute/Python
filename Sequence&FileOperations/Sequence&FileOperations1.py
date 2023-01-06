#1
#What is the output of the following code? nums =set([1,1,2,3,3,3,4,4])print(len(nums))
'''
The output of this code would be 4.

The set function creates a new set object, which is an unordered collection of unique elements.
When you pass the list [1,1,2,3,3,3,4,4] to the set function, it will remove any duplicates and create a set with the elements {1, 2, 3, 4}.
Then, when you call len() on this set object, it will return the number of elements in the set, which is 4.
'''

#2
#What will be the output? d ={"john":40, "peter":45} print(list(d.keys()))
'''
The output of this code would be ['john', 'peter'].

In this code, you are creating a dictionary called d with two key-value pairs, mapping the keys "john" and "peter" to the values 40 and 45, respectively. 
Then, you are calling the keys() method on the dictionary object d, which returns a view object that displays a list of all the keys in the dictionary. 
Finally, you are passing this view object to the list() function, which creates a new list object with the elements from the view object. 
This list object will contain the keys "john" and "peter", in the order they were added to the dictionary.
'''
#3
#A website requires a user to input username and password to register.
#Write a program to check the validity of password given by user.
#Following are the criteria for checking password:
    #1. At least 1 letter between [a-z]
    #2. At least 1 number between [0-9]
    #1. At least 1 letter between [A-Z]
    #3. At least 1 character from [$#@]
    #4. Minimum length of transaction password: 65.
    #Maximum length of transaction password: 12

import re

def is_valid_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[$#@]', password):
        return False
    return True

password = input('Enter password: ')
if is_valid_password(password):
    print('Valid password')
else:
    print('Invalid password')

#4
'''
Write a for loop that prints all elements of a list and their position in the list.a = [4,7,3,2,5,9]
'''
a = [4, 7, 3, 2, 5, 9]

for i, x in enumerate(a):
    print(f'{i}: {x}')


#5
'''
Please write a program which accepts a string from console and print the characters that have even indexes.
Example: If the following string is given as input to the program:H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:Helloworld
'''
string = input('Enter a string: ')
even_chars = string[::2]
print(even_chars)


#6
'''
Please write a program which accepts a string from console and print it in reverse order.
Example: If the following string is given as input to the program: rise to vote sir
Then, the output of the program should be:ris etov ot esir
'''

string = input('Enter a string: ')
print(string[::-1])

#7
'''
Please write a program which count and print the numbers of each character in a string input by console.
Example: If the following string is given as input to the program:abcdefgabc
Then, the output of the program should be:a,2c,2b,2e,1d,1g,1f,1
'''

string = input('Enter a string: ')
char_count = {}

for c in string:
    if c in char_count:
        char_count[c] += 1
    else:
        char_count[c] = 1

for c, count in char_count.items():
    print(f'{c},{count}', end=' ')

#8
'''
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155].
Write a program to make a list whose elements are intersection of the above given lists.
'''

list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]
intersection = [x for x in list1 if x in list2]
print(intersection)

#9
'''
With a given list [12,24,35,24,88,120,155,88,120,155].
Write a program to print this list after removing all duplicate values with original order reserved.
'''
lst = [12,24,35,24,88,120,155,88,120,155]
result = []

for x in lst:
    if x not in result:
        result.append(x)

print(result)


#10
'''
By using list comprehension, write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
'''
lst = [12,24,35,24,88,120,155]
result = [x for x in lst if x != 24]
print(result)


#11
'''
By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
'''

lst = [12,24,35,70,88,120,155]
result = [x for i, x in enumerate(lst) if i not in [0, 4, 5]]
print(result)


#12
'''
By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
'''

lst = [12,24,35,70,88,120,155]
result = [x for x in lst if x % 5 != 0 and x % 7 != 0]
print(result)

#13
'''
Pleas write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7, between 1 and 1000 inclusive.
'''

import random

numbers = []
while len(numbers) < 5:
    x = random.randint(1, 1000)
    if x % 5 == 0 and x % 7 == 0:
        numbers.append(x)

print(numbers)

#14
'''
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).Example:If the following n is given as input to the program:5Then, the output of the program should be:3.55
'''

n = int(input('Enter a positive integer: '))

sum = 0
for i in range(1, n+1):
    sum += i / (i+1)

print(sum)
