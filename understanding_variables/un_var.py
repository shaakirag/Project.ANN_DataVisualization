from all_libs import *

# Print the first few rows
def print_head(df):
    return df.head()

# Print the last few rows
def print_tail(df):
    return df.tail()

# Display a random number of records
def print_sample(df,n):
    return df.sample(n)

# View the number of rows and columns
def print_shape(df):
    return df.shape

# List of type of columns
def print_dtypes(df):
    return df.dtypes

# No. of NULL values
def print_info(df):
    return df.info()

# Statistical summary
def print_describe(df):
    return data.describe()
