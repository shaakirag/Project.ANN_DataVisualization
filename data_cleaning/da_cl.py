from pandas import *

# Dropping the duplicates
def drop_duplicates(df):
    df = df.drop_duplicates
    return df

# Replace no. of zeros with mean of those columns
def replace_zeros_mean(df, header_list):
    for h in header_list:
        df[h]=df[h].replace(0,df[h].mean())

# If the data uses '?' for missing values then we can replace them with a NaN
def replace_question_NaN(df):
    df = df.replace('?', np.NaN, inplace=True)
    return df

# Delete rows which contain missing values
def drop_NaN_rows(df):
    df = df.dropna()
    return df

# Delete rows
def drop_rows(df, row_list):
    df = df.drop(row_list, axis=0)
    return df

# Delete columns
def drop_columns(df, header_list):
    df = df.drop(header_list, axis=1)
    return df