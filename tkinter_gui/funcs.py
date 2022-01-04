from all_libs import *

def open_file(root, browse_txt, data):
    browse_txt.set('Loading...')
    while True:
        file = askopenfile(parent=root, mode='rb', title='Choose a file', filetype=[('csv file', '*.csv')])
        if file:
            while not isinstance(data, pd.DataFrame):
                data = pd.read_csv(file)
            break

    # Small text box under browse button
    file_name_box = tk.Text(root, height=1, width=20, padx=7)
    file_name_box.insert(1.0, os.path.basename(file.name))
    file_name_box.tag_configure('center', justify='center')
    file_name_box.tag_add('center', 1.0, 'end')
    file_name_box.grid(column=2, row=4)

    browse_txt.set('Browse')