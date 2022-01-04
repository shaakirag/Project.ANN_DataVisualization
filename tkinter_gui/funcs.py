from all_libs import *

def open_file(root, browse_txt):
    browse_txt.set('Loading...')
    file = askopenfile(parent=root, mode='rb', title='Choose a file', filetype=[('csv file', '*.csv')])
    if file:
        return pd.read_csv(file)
