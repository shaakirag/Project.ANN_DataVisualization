from pandas import *
import tkinter as tk

# Dropping the duplicates
def drop_duplicates(df):
    df = df.drop_duplicates

# Replace no. of zeros with mean of those columns
def replace_zeros_mean(df, header_list):
    for h in header_list:
        df[h]=df[h].replace(0,df[h].mean())

# If the data uses '?' for missing values then we can replace them with a NaN
def replace_question_NaN(df):
    df = df.replace('?', np.NaN, inplace=True)

# Delete rows which contain missing values
def drop_NaN_rows(df):
    df = df.dropna()

# Delete rows
def drop_rows(main_notebook, df, font):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='_Delete Rows')

    frame1 = tk.LabelFrame(frame, text='Set Input', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="Row Indices", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    rows_entry = tk.Entry(frame1, font=font)
    rows_entry.insert(10, 5)
    rows_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)

    set_head = tk.Button(frame1, text='Set Value',
                           command=lambda: set_row_field(rows_entry, df), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.04)


    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def set_row_field(rows_entry, df):
    df.drop(int(rows_entry.get()), axis=0, inplace=True)

# Delete columns
def drop_columns(main_notebook, df, font):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='_Delete Columns')

    frame1 = tk.LabelFrame(frame, text='Set Input', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="Header List", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    columns_entry = tk.Entry(frame1, font=font)
    columns_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)

    set_head = tk.Button(frame1, text='Set Value',
                           command=lambda: set_column_field(columns_entry, df), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.04)


    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def set_column_field(columns_entry, df):
    df.drop(columns_entry.get(), axis=1, inplace=True)