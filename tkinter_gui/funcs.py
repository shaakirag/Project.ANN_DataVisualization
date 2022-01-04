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
def open_file(root, frame, browse_txt, data):
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

# Adding Labels
def add_label(font):
    label = tk.Toplevel()
    label.title('Add Labels')
    frame = tk.Frame(label, bg='White', bd=5)
    frame.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)


    close = tk.Button(label, text='Close', command=label.destroy, font=font, bg='#008080', fg='White')
    close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)










