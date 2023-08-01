import pandas as pd

# Read the CSV file into a dataframe
df = pd.read_csv("")

# Get the number of rows and columns
print(df.shape)

# Get the data types of each column
print(df.dtypes)

# Calculate basic statistics for numeric columns
print(df.describe())

# Count the number of missing values in each column
print(df.isnull().sum())

# Select only certain columns
df = df[['name', 'net_price', 'date']]

# Group the data by name
df = df.groupby('name').sum()

# Filter rows based on a condition
df = df[df['net_price'] > 100]

import matplotlib.pyplot as plt

# Calculate the total sales by each customer
sales = df.groupby('name')['net_price'].sum()

# Plot the data
plt.bar(sales.index, sales.values)

# Label the axes
plt.xlabel('Customer Name')
plt.ylabel('Total Sales')

# Add a title
plt.title('Total Sales by Customer')

# Show the plot
plt.show()
