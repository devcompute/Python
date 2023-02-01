import pandas as pd
import matplotlib.pyplot as plt


# Load the sales data from the CSV file
df = pd.read_csv('/Users/benjaminadams/Downloads/777_m5_datasets_v1.0 2/BigMartSalesData.csv')

# Convert the 'Year-Month' column to a datetime and set it as the index
df['Year'] = pd.to_datetime(df['Year'])
df.set_index('Year', inplace=True)

# Filter the data to only include records from year 2011
df = df[df.index.year == 2011]

# Plot total sales per month for year 2011
plt.plot(df.index, df['Amount'], df['Month'])
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Total Sales Per Month for Year 2011')
plt.show()

# Find the month with the lowest total sales
min_month = df['Amount'].idxmin()
print(f'Month with lowest sales: {min_month.strftime("%B")}')

# Plot total sales per month for year 2011 as a bar chart
plt.bar(df.index, df['Amount'])
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Total Sales Per Month for Year 2011 (Bar Chart)')
plt.show()

# Group the data by 'Country' and sum the sales for each country
country_sales = df.groupby('Country')['Amount'].sum()

# Plot pie chart for year 2011 country-wise
plt.pie(country_sales, labels=country_sales.index)
plt.title('Sales by Country for Year 2011 (Pie Chart)')
plt.show()

# Plot scatter plot for invoice amounts
plt.scatter(df['Invoice Amount'], df['Other Variable'])
plt.xlabel('Invoice Amount')
plt.ylabel('Other Variable')
plt.title('Scatter Plot of Invoice Amounts')
plt.show()

# Plot kernel density estimate over scatter plot
sns.kdeplot(df['Invoice Amount'], df['Other Variable'])
plt.xlabel('Invoice Amount')
plt.ylabel('Other Variable')
plt.title('Scatter Plot of Invoice Amounts with KDE')
plt.show()
