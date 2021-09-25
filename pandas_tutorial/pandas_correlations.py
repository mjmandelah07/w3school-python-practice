# Pandas - Data Correlations
# Finding Relationships
# A great aspect of the Pandas module is the corr() method.
#
# The corr() method calculates the relationship between each column in your data set.
#
# The examples in this page uses a CSV file called: 'data.csv'.
#
# Download data.csv. or Open data.csv
#
# Example
# Show the relationship between the columns:
import pandas as pd

df = pd.read_csv("data.csv")
print(df.corr())

# What is a good correlation? It depends on the use,
# but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.
