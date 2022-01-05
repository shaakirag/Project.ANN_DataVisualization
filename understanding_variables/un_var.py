import tkinter as tk

# Print the first few rows
def head(df, font):
    head_ = tk.Toplevel()
    head_.title('Head')
    frame = tk.Frame(head_, bg='White', bd=5)
    frame.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)



    close = tk.Button(head_, text='Close', command=head_.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)
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
