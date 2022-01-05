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

# Group headers by their mean per each outcome
def mean_grouping(df, label):
    return df.groupby(label).mean()

# Statistical summary
def describe(df):
    return df.describe()
