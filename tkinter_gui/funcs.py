import os
import pandas as pd
from understanding_variables.un_var import *

# Instructions pop up
def instructions(main_notebook, font):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='Instructions')

    # Text box for instructions
    frame1 = tk.LabelFrame(frame, text='Instructions', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    instructions = tk.Label(frame1, text="Super long text",
                            font=font)
    instructions.pack()

    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)


# Uploading the file
def open_file(main_notebook, frame, menubar, filemenu, editmenu, browse_txt, df, font):
    browse_txt.set('Loading...')
    while True:
        file = tk.filedialog.askopenfile(parent=main_notebook, mode='rb', title='Choose a file', filetype=[('csv file', '*.csv')])
        if file:
            while not isinstance(df, pd.DataFrame):
                df = pd.read_csv(file)
            break

    # Small text box under browse button
    file_name_box = tk.Text(frame, height=1, width=20, padx=7)
    file_name_box.insert(1.0, os.path.basename(file.name))
    file_name_box.tag_configure('center', justify='center')
    file_name_box.tag_add('center', 1.0, 'end')
    # file_name_box.grid(column=2, row=4)
    file_name_box.place(relx=0.3, rely=0.85, relwidth=0.4, relheight=0.04)

    browse_txt.set('Browse')

    set_menu_label = tk.Button(frame, text='Next', command=lambda:set_label_menu(main_notebook, menubar, filemenu, editmenu, font, df), font=font, bg='#008080', fg='White')
    set_menu_label.place(relx=0.9, rely=0.95, relwidth=0.1, relheight=0.04)

def set_label_menu(main_notebook, menubar, filemenu, editmenu, font, df):
    if filemenu.index('end') is not None:
        for i in range(filemenu.index('end') + 1):
            if filemenu.entrycget(i, 'label') == 'Add Labels':
                filemenu.delete('Add Labels')
                menubar.delete('Actions')

    filemenu.add_command(label="Add Labels", command=lambda: add_label(main_notebook, menubar, editmenu, font, df))
    menubar.add_cascade(label="Actions", menu=filemenu)

class Label:
    def __init__(self, type_of_label):
        self.type = type_of_label
        self.label = 'Not Assigned'

    def label_func(self, label_entry):
        self.label = label_entry.get()


# Adding Labels
def add_label(main_notebook, menubar, editmenu, font, df):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='Labels')

    frame1 = tk.LabelFrame(frame, text='Instructions', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame1, text="Label", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    tk.Label(frame1, text="Label 0", font=font).place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)
    tk.Label(frame1, text="Label 1", font=font).place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.1)

    label_entry = tk.Entry(frame1, font=font)
    label_0_entry = tk.Entry(frame1, font=font)
    label_1_entry = tk.Entry(frame1, font=font)

    label_entry.insert(10, "Outcome")
    label_0_entry.insert(10, "Negative")
    label_1_entry.insert(10, "Positive")

    label_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)
    label_0_entry.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.04)
    label_1_entry.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.04)

    label_entry_outcome = Label('Outcome')
    label_0_entry_negative = Label('Negative')
    label_1_entry_positive = Label('Positive')

    set_values = tk.Button(frame1, text='Set Values', command=lambda: set_value_fields(main_notebook, [[label_entry, label_entry_outcome],
                                                                          [label_0_entry, label_0_entry_negative],
                                                                          [label_1_entry, label_1_entry_positive]],
              menubar, editmenu, font, df), font=font, bg='#008080', fg='White')
    set_values.place(relx=0.4, rely=0.9, relwidth=0.2,relheight=0.04)

    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def set_value_fields(main_notebook, labels, menubar, editmenu, font, df):
    for l in labels:
        l[1].label_func(l[0])

    if editmenu.index('end') is not None:
        for i in range(editmenu.index('end') + 1):
            if editmenu.entrycget(i, 'label') == 'Cleaning Data':
                editmenu.delete('Cleaning Data')
                editmenu.delete('Understanding Your Variables')
                menubar.delete('Pre-Processing')

    editmenu.add_command(label="Understanding Your Variables", command=lambda: understanding_your_variables(main_notebook, font, df))
    editmenu.add_command(label="Cleaning Data", command=lambda: add_label(menubar, font))
    menubar.add_cascade(label='Pre-Processing', menu=editmenu)

def understanding_your_variables(main_notebook, font, df):
    frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
    frame.pack(fill='both', expand=1)

    main_notebook.add(frame, text='Understanding Your Variables')

    frame1 = tk.LabelFrame(frame, text='Select a Command', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Button(frame1, text='Head', command=lambda:head(main_notebook, df, font), font=font, bg='#008080', fg='White').place(relx=0.225, rely=0.05, relwidth=0.5, relheight=0.05)
    tk.Button(frame1, text='Tail', command=lambda:tail(main_notebook, df, font), font=font, bg='#008080', fg='White').place(relx=0.225, rely=0.16, relwidth=0.5, relheight=0.05)
    tk.Button(frame1, text='Sample', command=lambda:sample(main_notebook, df, font), font=font, bg='#008080', fg='White').place(relx=0.225, rely=0.27, relwidth=0.5, relheight=0.05)
    tk.Button(frame1, text='Row and Column Number', font=font, bg='#008080', fg='White').place(relx=0.225, rely=0.38, relwidth=0.5, relheight=0.05)
    tk.Button(frame1, text='Column Types', font=font, bg='#008080', fg='White').place(relx=0.225, rely=0.49, relwidth=0.5, relheight=0.05)
    tk.Button(frame1, text='NULL Info', font=font, bg='#008080', fg='White').place(relx=0.225, rely=0.6, relwidth=0.5, relheight=0.05)
    tk.Button(frame1, text='Mean per Label', font=font, bg='#008080', fg='White').place(relx=0.225, rely=0.71, relwidth=0.5, relheight=0.05)
    tk.Button(frame1, text='Statistical Summary', font=font, bg='#008080', fg='White').place(relx=0.225, rely=0.82, relwidth=0.5, relheight=0.05)

    close = tk.Button(frame, text='Close', command=frame.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)




