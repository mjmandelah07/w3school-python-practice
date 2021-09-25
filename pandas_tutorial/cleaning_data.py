# Data Cleaning
# Data cleaning means fixing bad data in your data set.
#
# Bad data could be:
#
# Empty cells
# Data in wrong format
# Wrong data
# Duplicates

# Empty Cells
# Empty cells can potentially give you a wrong result when you analyze data.
#
# Remove Rows
# One way to deal with empty cells is to remove rows that contain empty cells.
#
# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
#
# Example
# Return a new Data Frame with no empty cells:
import pandas as pd

df = pd.read_csv("dirtydata.csv")

new_df = df.dropna()
print(new_df.to_string())

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
#
# If you want to change the original DataFrame, use the inplace = True argument:
#
# Example
# Remove all rows with NULL values:

# df = pd.read_csv('dirtydata.csv')

# df.dropna(inplace=True)
# print(df.to_string())

# Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.
#
# This way you do not have to delete entire rows just because of some empty cells.
#
# The fillna() method allows us to replace empty cells with a value:
#
# Example
# Replace NULL values with the number 130:
import pandas as pd

df = pd.read_csv('dirtydata.csv')

df.fillna(130, inplace=True)

print(df.to_string())

# Replace Only For a Specified Columns
# The example above replaces all empty cells in the whole Data Frame.
#
# To only replace empty values for one column, specify the column name for the DataFrame:
#
# Example
# Replace NULL values in the "Calories" columns with the number 130:
import pandas as pd

df = pd.read_csv('dirtydata.csv')

df["Calories"].fillna(130, inplace=True)

print(df.to_string())

# Replace Using Mean, Median, or Mode
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
#
# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:
#
# Example
# Calculate the MEAN, and replace any empty values with it:
import pandas as pd

df = pd.read_csv('dirtydata.csv')
x = df["Calories"].mean()

df["Calories"].fillna(x, inplace=True)

print(df.to_string())

# Mean = the average value (the sum of all values divided by number of values).
#
# Example
# Calculate the MEDIAN, and replace any empty values with it:
import pandas as pd

df = pd.read_csv('dirtydata.csv')
x = df["Calories"].median()

df["Calories"].fillna(x, inplace=True)

print(df.to_string())

# Median = the value in the middle, after you have sorted all values ascending.
#
# Example
# Calculate the MODE, and replace any empty values with it:
import pandas as pd

df = pd.read_csv('dirtydata.csv')
x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace=True)

print(df.to_string())

# Pandas - Cleaning Data of Wrong Format
# Data of Wrong Format
# Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
#
# To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
#
# Convert Into a Correct Format
# In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, t
# he 'Date' column should be a string that represents a date:
# Let's try to convert all cells in the 'Date' column into dates.
#
# Pandas has a to_datetime() method for this:
#
# Example
# Convert to date:
import pandas as pd

df = pd.read_csv('dirtydata.csv')

df['Date'] = pd.to_datetime(df['Date'])
df.dropna(subset=['Date'], inplace=True)  # Remove rows with a NULL value in the "Date" column:

print(df.to_string())

# Fixing wrong data
# Example
# Set "Duration" = 45 in row 7:
import pandas as pd

df = pd.read_csv('dirtydata.csv')

df.loc[7, "Duration"] = 45

print(df.to_string())

# Example
# Loop through all values in the "Duration" column.
#
# If the value is higher than 120, set it to 120:
import pandas as pd

df = pd.read_csv('dirtydata.csv')

for x in df.index:
    if df.loc[7, "Duration"] > 60:
        df.loc[7, "Duration"] = 55

print(df.to_string())

# Example
# Delete rows where "Duration" is higher than 120:
import pandas as pd

df = pd.read_csv('data.csv')

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)

print(df.to_string())

# Example
# Returns True for every row that is a duplicate, othwerwise False:
import pandas as pd

df = pd.read_csv('data.csv')

print(df.duplicated())

# Removing Duplicates
# To remove duplicates, use the drop_duplicates() method.
#
# Example
# Remove all duplicates:
import pandas as pd

df = pd.read_csv('data.csv')

df.drop_duplicates(inplace = True)

print(df.to_string())


