# What is a DataFrame?
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
#
# Example
# Create a simple Pandas DataFrame:
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

# Locate Row
# As you can see from the result above, the DataFrame is like a table with rows and columns.
#
# Pandas use the loc attribute to return one or more specified row(s)
#
# Example
# Return row 0:
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df.loc[0:2])

# Named Indexes
# With the index argument, you can name your own indexes.
#
# Example
# Add a list of names to give each row a name:
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)


# Locate Named Indexes
# Use the named index in the loc attribute to return the specified row(s).
#
# Example
# Return "day2":
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df.loc["day3"])

# to return the entire dataframe
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df.to_string())


