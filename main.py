import tkinter

import pandas as pd

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

font = 'Raleway'

root = tk.Tk()


canvas = tk.Canvas(root, width=1000, height=600)
canvas.grid(columnspan=5, rowspan=5)

set_logo('tkinter_gui/images/logo.png')

# Welcome message
welcome = tk.Label(root, text = 'Upload a dataset to continue', font = font)
welcome.grid(columnspan=1, column=2, row=1)

# Browse button
browse_txt = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_txt, font=font, bg='#008080', fg='White', height=2, width=15)
browse_txt.set('Browse')
browse_btn.grid(column=2, row=3)

df = False
while not isinstance(df, pd.DataFrame):
    df = open_file(root, browse_txt)



root.mainloop()
