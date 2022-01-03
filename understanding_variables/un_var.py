from all_libs import *

# Print the first few rows
def head(df):
    return df.head()

# Print the last few rows
def tail(df):
    return df.tail()

# Display a random number of records
def sample(df,n):
    return df.sample(n)

# View the number of rows and columns
def shape(df):
    return df.shape

# List of type of columns
def dtypes(df):
    return df.dtypes

# No. of NULL values
def info(df):
    return df.info()

# Statistical summary
def describe(df):
    return data.describe()
