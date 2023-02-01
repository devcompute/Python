"""
1. Extract data from the given SalaryGender CSV file and store the data from each
column in a separate NumPy array
"""
#Install NumPy and Pandas with pip using temrinal window command below.
pip install numpy pandas

#Use code below to extract data.
import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('SalaryGender.csv')

# Extract the data from the 'Salary' column and store it in a NumPy array
salary_data = df['Salary'].to_numpy()

# Extract the data from the 'Gender' column and store it in a NumPy array
gender_data = df['Gender'].to_numpy()

'''
2. Find:
1. The number of men with a PhD
2. The number of women with a PhD
'''

import pandas as pd

df = pd.read_csv('SalaryGender.csv')

# Create a DataFrame for male data
male_df = df.loc[df['Gender'] == 'Male']

# Create a DataFrame for female data
female_df = df.loc[df['Gender'] == 'Female']

# Count the number of men with a PhD
num_men_phd = male_df['PhD'].count()

# Count the number of women with a PhD
num_women_phd = female_df['PhD'].count()


'''
3. Store the “Age” and “PhD” columns in one DataFrame and delete the data of all
people who don’t have a PhD from SalaryGender CSV file.
'''

import pandas as pd

df = pd.read_csv('SalaryGender.csv')

# Create a new DataFrame with the "Age" and "PhD" columns
age_phd_df = df[['Age', 'PhD']]

# Delete the data of all people who don't have a PhD
age_phd_df = age_phd_df.dropna()


'''
4. Calculate the total number of people who have a PhD degree from SalaryGender
CSV file.
'''

import pandas as pd

df = pd.read_csv('SalaryGender.csv')

# Calculate the total number of people who have a PhD degree
total_phds = df['PhD'].count()


'''
5. How do you Count The Number Of Times Each Value Appears In An Array Of
Integers?
[0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
Answer should be array([4, 2, 1, 1, 3, 2, 0, 0, 0, 1]) which means 0 comes 4 times,
1 comes 2 times, 2 comes 1 time, 3 comes 1 time and so on.
'''

import numpy as np

# Create an array of integers
arr = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])

# Use numpy.bincount to count the number of times each value appears
counts = np.bincount(arr)

# Print the counts
print(counts)


'''
6. Create a numpy array [[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]]) and filter the elements
greater than 5.
'''

import numpy as np

# Create a NumPy array
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])

# Filter the elements that are greater than 5
filtered_arr = np.where(arr > 5)

# Print the filtered array
print(filtered_arr)


'''
7. Create a numpy array having NaN (Not a Number) and print it.
array([ nan, 1., 2., nan, 3., 4., 5.])
Print the same array omitting all elements which are nan
'''

import numpy as np

# Create a NumPy array with NaN values
arr = np.array([np.nan, 1., 2., np.nan, 3., 4., 5.])

# Print the array
print(arr)

# Filter the NaN values
filtered_arr = np.where(~np.isnan(arr))

# Print the filtered array
print(filtered_arr)


# Select the non-NaN values from the original array
filtered_values = arr[filtered_arr]

# Print the filtered values
print(filtered_values)


'''
8. Create a 10x10 array with random values and find the minimum and maximum
values.
'''

import numpy as np

# Create a 10x10 array with random values
arr = np.random.rand(10, 10)

# Find the minimum and maximum values
minimum = np.min(arr)
maximum = np.max(arr)

# Print the minimum and maximum values
print(f"Minimum value: {minimum}")
print(f"Maximum value: {maximum}")


'''
9. Create a random vector of size 30 and find the mean value.
'''

import numpy as np

# Create a random vector of size 30
vec = np.random.rand(30)

# Find the mean value
mean_value = vec.mean()

# Print the mean value
print(f"Mean value: {mean_value}")


'''
10. Create numpy array having elements 0 to 10 And negate all the elements between
3 and 9
'''

import numpy as np

# Create a NumPy array with elements 0 to 10
arr = np.arange(11)

# Negate all the elements between 3 and 9
arr[3:10] = -arr[3:10]

# Print the modified array
print(arr)


'''
11. Create a random array of 3 rows and 3 columns and sort it according to 1st column,
2nd column or 3rd column.
'''

import numpy as np

# Create a random array of 3 rows and 3 columns
arr = np.random.rand(3, 3)

# Sort the array according to the 1st column
sorted_arr = arr[arr[:,0].argsort()]

# Print the sorted array
print(sorted_arr)

# Sort the array according to the 2nd column
sorted_arr = arr[arr[:,1].argsort()]

# Print the sorted array
print(sorted_arr)

# Sort the array according to the 3rd column
sorted_arr = arr[arr[:,2].argsort()]

# Print the sorted array
print(sorted_arr)

'''
12. Create a four dimensions array get sum over the last two axis at once.
'''

import numpy as np

# Create a four-dimensional array
arr = np.random.rand(2, 3, 4, 5)

# Get the sum over the last two axes
sum_last_two_axes = np.sum(arr, axis=(-2, -1))

# Print the sum
print(sum_last_two_axes)


'''
13. Create a random array and swap two rows of an array.
'''

import numpy as np

# Create a random array
arr = np.random.rand(3, 3)

# Swap the first and third rows
arr[[0, 2]] = arr[[2, 0]]

# Print the modified array
print(arr)

# Swap the first and third rows using numpy.swapaxes
arr = np.swapaxes(arr, 0, 1)[:, [2, 0, 1]]

# Print the modified array
print(arr)

'''
14. Create a random matrix and Compute a matrix rank.
'''

import numpy as np

# Create a random matrix
mat = np.random.rand(3, 3)

# Compute the matrix rank
rank = np.linalg.matrix_rank(mat)

# Print the rank
print(f"Matrix rank: {rank}")


'''
15.Analyse various school outcomes in Tennessee using pandas. Suppose you are a
public school administrator. Some schools in your state of Tennessee are
performing below average academically. Your superintendent, under pressure
from frustrated parents and voters, approached you with the task of understanding
why these schools are under-performing. To improve school performance, you
need to learn more about these schools and their students, just as a business needs
to understand its own strengths and weaknesses and its customers. Though you is
eager to build an impressive explanatory model, you know the importance of
conducting preliminary research to prevent possible pitfalls or blind spots. Thus,
you engages in a thorough exploratory analysis, which includes: a lit review, data
collection, descriptive and inferential statistics, and data visualization.

Phase 1 - Data Collection
Here is a data of every public school in middle Tennessee. The data also includes
various demographic, school faculty, and income variables. You need to convert the
data into useful information.
• Read the data in pandas data frame
• Describe the data to find more details



Phase 2 - Group data by school ratings
Chooses indicators that describe the student body (for example, reduced_lunch) or
school administration (stu_teach_ratio) hoping they will
explain school_rating. reduced_lunch is a variable measuring the average percentage
of students per school enrolled in a federal program that provides lunches for students
from lower-income households. In short, reduced_lunch is a good proxy for household
income.
Isolates ‘reduced_lunch’ and groups the data by ‘school_rating’ using pandas groupby
method and then uses describe on the re-shaped data

Phase 3 – Correlation analysis
Find the correlation between ‘reduced_lunch’ and ‘school_rating’. The values in the
correlation matrix table will be between -1 and 1. A value of -1 indicates the strongest
possible negative correlation, meaning as one variable decreases the other increases.
And a value of 1 indicates the opposite.

Phase 4 – Scatter Plot
Find the relationship between school_rating and reduced_lunch, Plot a graph with the
two variables on a scatter plot. Each dot represents a school. The placement of the dot
represents that school's rating (Y-axis) and the percentage of its students on reduced
lunch (x-axis). The downward trend line shows the negative correlation
between school_rating and reduced_lunch (as one increases, the other decreases). The
slope of the trend line indicates how much school_rating decreases
as reduced_lunch increases. A steeper slope would indicate that a small change
in reduced_lunch has a big impact on school_rating while a more horizontal slope
would indicate that the same small change in reduced_lunch has a smaller impact
on school_rating.

Phase 5 – Correlation Matrix
An efficient graph for assessing relationships is the correlation matrix, as seen below;
its color-coded cells make it easier to interpret than the tabular correlation matrix
above. Red cells indicate positive correlation; blue cells indicate negative correlation;
white cells indicate no correlation. The darker the colors, the stronger the correlation
(positive or negative) between those two variables. Draw a graph of correlation matrix
having all important fields of data frame.
'''

#Phase1

import pandas as pd

# Read the data in a pandas DataFrame
df = pd.read_csv("school_data.csv")

# Describe the data to find more details
df.describe()


#Phase2

# Group the data by 'school_rating' and describe the 'reduced_lunch' column
df.groupby("school_rating")["reduced_lunch"].describe()


#Phase3

# Find the correlation between 'reduced_lunch' and 'school_rating'
df["reduced_lunch"].corr(df["school_rating"])


#Phase4

import matplotlib.pyplot as plt

# Plot a scatter plot with 'school_rating' on the y-axis and 'reduced_lunch' on the x-axis
plt.scatter(df["reduced_lunch"], df["school_rating"])

# Add a trend line showing the negative correlation between 'school_rating' and 'reduced_lunch'
plt.plot(df["reduced_lunch"], np.poly1d(np.polyfit(df["reduced_lunch"], df["school_rating"], 1))(df["reduced_lunch"]))

# Show the plot
plt.show()


#Phase5

import seaborn as sns

# Compute the correlations between all the columns
corr = df.corr()

# Use seaborn to visualize the correlations in a heatmap
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns)

# Show the plot
plt.show()


