import tkinter as tk
import matplotlib
matplotlib.use("TKAgg")

# Print the first few rows
def head(main_notebook, df, font):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='_Head')

    frame1 = tk.LabelFrame(frame, text='Set Input', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="No. of Rows", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    head_entry = tk.Entry(frame1, font=font)
    head_entry.insert(10, 5)
    head_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)

    set_head = tk.Button(frame1, text='Set Value',
                           command=lambda: set_head_field(head_entry, frame1, df, font), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.04)


    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def set_head_field(head_entry, frame1, df, font):
    rows = int(head_entry.get())
    head_ = df.head(rows)
    output = tk.Label(frame1, text=head_, font=(font, 8))
    output.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# Print the last few rows
def tail(main_notebook, df, font):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='_Tail')

    frame1 = tk.LabelFrame(frame, text='Set Input', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="No. of Rows", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    tail_entry = tk.Entry(frame1, font=font)
    tail_entry.insert(10, 5)
    tail_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)

    set_head = tk.Button(frame1, text='Set Value',
                           command=lambda: set_tail_field(tail_entry, frame1, df, font), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.04)


    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def set_tail_field(tail_entry, frame1, df, font):
    rows = int(tail_entry.get())
    tail_ = df.tail(rows)
    output = tk.Label(frame1, text=tail_, font=(font, 8))
    output.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# Display a random number of records
def sample(main_notebook, df, font):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='_Sample')

    frame1 = tk.LabelFrame(frame, text='Set Input', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="No. of Rows", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    sample_entry = tk.Entry(frame1, font=font)
    sample_entry.insert(10, 5)
    sample_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)

    set_head = tk.Button(frame1, text='Set Value',
                           command=lambda: set_sample_field(sample_entry, frame1, df, font), font=font, bg='#008080',fg='White')
    set_head.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.04)


    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def set_sample_field(sample_entry, frame1, df, font):
    rows = int(sample_entry.get())
    sample_ = df.tail(rows)
    output = tk.Label(frame1, text=sample_, font=(font, 8))
    output.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

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
