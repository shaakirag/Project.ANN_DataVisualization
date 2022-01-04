from all_libs import *
from understanding_variables.un_var import *
from data_cleaning.da_cl import *
from visualization.basic_analysis import *
from visualization.comparative_analysis import *
from visualization.probabilistic_analysis import *
from prediction_ann.model_ann.ann_model import *
from prediction_ann.model_ann.ann_test import *
from prediction_ann.model_ann.backward_propagation import *
from prediction_ann import *
from tkinter_gui.funcs import *
from tkinter_gui.images import *
from tkinter_gui.images.images import *

HEIGHT = 1000
WIDTH = 700

font = 'Raleway'

root = tk.Tk()


canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.grid(columnspan=5, rowspan=5)

frame = tk.Frame(root)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.9)

set_logo('tkinter_gui/images/logo.png')

# Welcome message
welcome = tk.Label(frame, text = 'Upload a dataset to continue', font = font)
#welcome.grid(columnspan=1, column=2, row=1)
welcome.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.05)

# Browse button
browse_txt = tk.StringVar()
browse_btn = tk.Button(frame, textvariable=browse_txt, command=lambda:open_file(root, frame, browse_txt, False), font=font, bg='#008080', fg='White', height=2, width=15)
browse_txt.set('Browse')
#browse_btn.grid(column=2, row=3)
browse_btn.place(relx=0.425, rely=0.77, relwidth=0.15, relheight=0.05)

root.mainloop()
