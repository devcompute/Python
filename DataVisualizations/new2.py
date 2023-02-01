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
