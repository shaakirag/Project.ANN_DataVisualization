import tkinter

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
canvas.pack()

# Welcome Page

#Does not work
#set_background(root, 'tkinter_gui/images/background.png')

frame = tk.Frame(root, bg = 'White', bd=5)
frame.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)

set_logo(frame, 'tkinter_gui/images/logo.png')

# Menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

root.config(menu=menubar)

# Instructions message
instructions_txt = tk.StringVar()
instructions_btn = tk.Button(frame, textvariable=instructions_txt, command=lambda:instructions(font), font=font, bg='White', fg='Black', height=2, width=15)
instructions_txt.set('Instructions')
instructions_btn.place(relx=0.325, rely=0.7, relwidth=0.35, relheight=0.05)

# Browse button
browse_txt = tk.StringVar()
browse_btn = tk.Button(frame, textvariable=browse_txt, command=lambda:open_file(root, frame, browse_txt, False, filemenu, menubar, font), font=font, bg='#008080', fg='White', height=2, width=15)
browse_txt.set('Browse')
#browse_btn.grid(column=2, row=3)
browse_btn.place(relx=0.425, rely=0.77, relwidth=0.15, relheight=0.05)



close = tk.Button(root, text='Close', command=root.destroy, font=font, bg='Black', fg='White')
close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)


root.mainloop()
