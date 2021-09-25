# Viewing the Data
# One of the most used method for getting a quick overview of the DataFrame, is the head() method.
#
# The head() method returns the headers and a specified number of rows, starting from the top.
#
# Example
# Get a quick overview by printing the first 10 rows of the DataFrame:
import pandas as pd

df = pd.read_csv("data.csv")

print("Printing the first 10 rows of the DataFrame:")
print(df.head(10))
print("\n")

# Note: if the number of rows is not specified, the head() method will return the top 5 rows.
#
# Example
# Print the first 5 rows of the DataFrame:
import pandas as pd

df = pd.read_csv("data.csv")

print("Printing the first 5 rows of the DataFrame:")
print(df.head())
print("\n")

# There is also a tail() method for viewing the last rows of the DataFrame.
#
# The tail() method returns the headers and a specified number of rows, starting from the bottom.
#
# Example
# Print the last 5 rows of the DataFrame:
print("Printing the first 5 rows of the DataFrame:")
print(df.tail())
print("\n")

# Info About the Data
# The DataFrames object has a method called info(), that gives you more information about the data set.
#
# Example
# Print information about the data:
print("The information about data:")
print(df.info())
