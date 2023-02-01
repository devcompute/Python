"""
Business challenge/requirement
BigMart is one of the biggest retailer of Europe and has operations across multiple
countries. You are a data analyst in IT team of BigMart. Invoice and SKU wise Sales
Data for Year 2011 is shared with you. You need to prepare meaningful charts to
show case the various sales trends for 2011 to top management.

Key issues
Data should be displayed pictorially to capture the attention of top management

Considerations
NONE

Data volume
- Approx 500K records – file BigMartSalesData.csv

Additional information
- NA

Business benefits
This exercise is an annual exercise and BigMart makes important investment
decision based on trends

Approach to Solve
You have to use fundamentals of Matplotlib covered in module 5 and plot following 4
chart/graph

    1. Plot Total Sales Per Month for Year 2011. How the total sales have increased
    over months in Year 2011. Which month has lowest Sales?
    2. Plot Total Sales Per Month for Year 2011 as Bar Chart. Is Bar Chart Better to
    visualize than Simple Plot?
    3. Plot Pie Chart for Year 2011 Country Wise. Which Country contributes highest
    towards sales?
    4. Plot Scatter Plot for the invoice amounts and see the concentration of amount.
    In which range most of the invoice amounts are concentrated

Enhancements for code
You can try these enhancements in code
    1. Change the bar chart to show the value of bar
    2. In Pie Chart Play With Parameters shadow=True, startangle=90 and see how
    different the chart looks
    3. In scatter plot change the color of Scatter Points
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file into a Pandas data frame
df = pd.read_csv('/Users/benjaminadams/Downloads/777_m5_datasets_v1.0 2/BigMartSalesData.csv')

# Convert the date column to a datetime data type
df['date'] = pd.to_datetime(df['Day'])

# Extract the month and year from the date column and create a new column called 'month_year'
df['Month'] = df['date'].dt.strftime('%m/%Y')

# Group the data by 'month_year' and calculate the total sales for each month
monthly_sales = df.groupby('Year')['Amount'].sum().reset_index()

# Rename the 'sales' column to 'Amount'
monthly_sales.rename(columns={'sales': 'Amount'}, inplace=True)

# Plot the total sales by month using a line chart
plt.plot(monthly_sales['Year'], monthly_sales['Amount'])
plt.xlabel('Month/Year')
plt.ylabel('Total Sales')
plt.title('Total Sales Per Month for Year 2011')
plt.show()

# Plot the total sales by month using a bar chart
monthly_sales.plot(x='Year', y='Amount', kind='bar')
plt.xlabel('Month/Year')
plt.ylabel('Total Sales')
plt.title('Total Sales Per Month for Year 2011')
plt.show()

# Group the data by 'country' and calculate the total sales for each country
country_sales = df.groupby('Country')['Amount'].sum().reset_index()

# Plot a pie chart showing the total sales by country
plt.pie(country_sales['Amount'], labels=country_sales['Country'], shadow=True, startangle=90)
plt.axis('equal')
plt.title('Total Sales by Country for Year 2011')
plt.show()

# Plot a scatter plot showing the relationship between the invoice amount and the concentration of amounts
df.plot.scatter(x='Amount', y='Quantity')
plt.xlabel('Invoice Amount')
plt.ylabel('Concentration')
plt.title('Invoice Amount vs. Concentration')
plt.show()
