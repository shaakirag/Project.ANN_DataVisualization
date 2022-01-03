from all_libs import *

# Dropping the duplicates
def drop_duplicates(df):
    df = df.drop_duplicates
    return df

# Number of NULLS for each header
def check_null(df):
    return df.isnull().sum()

# Check the number of zero values in a dataset
def number_zero_values(df, header_list):
    h_zero_list = []
    for h in header_list:
        h_tuple = (h, df[df[h]==0.0].shape[0])
        h_zero_list.append(h_tuple)
    return h_zero_list

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