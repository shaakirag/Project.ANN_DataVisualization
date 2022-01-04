import tkinter

from all_libs import *

# Instructions pop up
def instructions(font):
    inst = tk.Toplevel()
    inst.title('Instructions')
    frame = tk.Frame(inst, bg='White', bd=5)
    frame.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    # Text box for instructions
    frame1 = tk.LabelFrame(frame, text='Instructions', font=font)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    instructions = tk.Label(frame1, text="Super long text",
                         font=font)
    instructions.pack()

    close = tk.Button(inst, text='Close', command=inst.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

# Uploading the file
def open_file(root, frame, browse_txt, data, filemenu, menubar, font):
    browse_txt.set('Loading...')
    while True:
        file = askopenfile(parent=root, mode='rb', title='Choose a file', filetype=[('csv file', '*.csv')])
        if file:
            while not isinstance(data, pd.DataFrame):
                data = pd.read_csv(file)
            break

    # Small text box under browse button
    file_name_box = tk.Text(frame, height=1, width=20, padx=7)
    file_name_box.insert(1.0, os.path.basename(file.name))
    file_name_box.tag_configure('center', justify='center')
    file_name_box.tag_add('center', 1.0, 'end')
    #file_name_box.grid(column=2, row=4)
    file_name_box.place(relx=0.3, rely=0.85, relwidth=0.4, relheight=0.04)

    browse_txt.set('Browse')

    filemenu.add_command(label="Add Labels", command=lambda: add_label(font))
    menubar.add_cascade(label="Actions", menu=filemenu)

class Label:
  def __init__(self, type_of_label):
    self.type = type_of_label
    self.label = 'Not Assigned'

  def label_func(self, label_entry):
      self.label = label_entry.get()

# Adding Labels
def add_label(font):
    label = tk.Toplevel()
    label.title('Add Labels')
    frame = tk.Frame(label, bg='White', bd=5)
    frame.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

    tk.Label(frame, text="Label", font=font).place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)
    tk.Label(frame, text="Label 0",font=font).place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)
    tk.Label(frame, text="Label 1", font=font).place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.1)

    label_entry = tk.Entry(frame, font=font)
    label_0_entry = tk.Entry(frame, font=font)
    label_1_entry = tk.Entry(frame, font=font)

    label_entry.insert(10, "Outcome")
    label_0_entry.insert(10, "Negative")
    label_1_entry.insert(10, "Positive")

    label_entry.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.04)
    label_0_entry.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.04)
    label_1_entry.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.04)

    label_entry_outcome = Label('Outcome')
    label_0_entry_negative = Label('Negative')
    label_1_entry_positive = Label('Positive')

    tk.Button(frame, text='Set Values', command=lambda:set_value_fields([[label_entry, label_entry_outcome],
                                                                         [label_0_entry, label_0_entry_negative],
                                                                         [label_1_entry, label_1_entry_positive]]),
                                                                        font=font, bg='#008080', fg='White').place(relx=0.4,
                                                                                                                   rely=0.9,
                                                                                                                   relwidth=0.2,
                                                                                                                   relheight=0.04)

    close = tk.Button(label, text='Close', command=label.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

def set_value_fields(labels):
    for l in labels:
        l[1].label_func(l[0])















