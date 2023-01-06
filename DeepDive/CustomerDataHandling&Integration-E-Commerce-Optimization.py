'''
Business challenge/requirement
GoodsKart—largest ecommerce company of Indonesia with revenue of $2B+
acquired another ecommerce company FairDeal. FairDeal has its own IT system to
maintain records of customer, sales etc. For ease of maintenance and cost savings
GoodsKart is integrating customer databases of both the organizations hence
customer data of FairDeal has to be converted in GoodsKart Customer Format.

Key issues
GoodsKart customer data has more fields than in FairDeal customer data. Hence
FairDeal data needs to be split and stored in GoodsKart Customer Object Oriented
Data Structure

Considerations
System should convert the data at run time

Data volume
- NA

Additional information
- NA

Business benefits
GoodsKart can eventually sunset IT systems of FairDeal and reduce IT cost by 20-
30%

Approach to Solve
You have to use fundamentals of Python taught in module 3.
1. Read FairDealCustomerData.csv
2. Name field contains full name – use regular expression to separate title, first
name, last name
3. Store the data in Customer Class
4. Create Custom Exception – CustomerNotAllowedException
5. Pass a customer to function "createOrder" and throw

CustomerNotAllowedException in case of blacklisted value is 1
Enhancements for code
You can try these enhancements in code
1. Change function createOrder to take productname and product code as input
2. Create Class Order.
'''
'''
#Return object of type Order in case customer is eligible.
'''


import re
import csv

class CustomerNotAllowedException(Exception):
    pass

class Customer:
    def __init__(self, title, first_name, last_name, email, blacklisted):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.blacklisted = blacklisted

class Order:
    def __init__(self, customer, product_name, product_code):
        self.customer = customer
        self.product_name = product_name
        self.product_code = product_code

def create_order(customer, product_name, product_code):
    if customer.blacklisted == 1:
        raise CustomerNotAllowedException('Customer is blacklisted')
    else:
        # Create the Order object and save it to the database
        order = Order(customer, product_name, product_code)
        save_to_database(order)

def save_to_database(order):
    pass

# Read the FairDeal customer data from the CSV file
with open('FairDealCustomerData.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row['Name']
        email = row['Email']
        blacklisted = row['Blacklisted']

        # Use a regular expression to split the name into title, first name, and last name
        match = re.match(r'([\w ]+)\s([\w]+)\s([\w]+)', name)
        title = match.group(1)
        first_name = match.group(2)
        last_name = match.group(3)

        # Create a Customer object and pass it to the create_order function
        customer = Customer(title, first_name, last_name, email, blacklisted)
        create_order(customer, 'product name', 'product code')

#The code in python above reads the 'FairDealCustomerData.csv" file with using a regular expression to seperate titles of the first and last name in the 'Name' field.
#This creates 'Customer' class to store the customer data in which the class has attributes for the columns in the file.
#This creates 'CustomerNotAllowedException' to alert when a customer is blacklisted.
#The function 'create_order()' is defined for a 'Customer' object and product name and code for the input.
#This checks to see if the customer is blacklisted for the 'Blacklisted' field in the 'Customer' object.
#If the customer is blacklisted then the function has raised the 'CustomernotAllowedException' exception.
#If the customer is not blacklisted then the 'Order' is returned.
#Defining the 'Order' class to store the order data in which the class should have attributes for each category.
#The 'create_order()' function handles more complex orders with multiple products or quantities.
#This saves the information in 'save_to_database.'



