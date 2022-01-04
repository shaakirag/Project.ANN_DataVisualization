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
from tkinter_gui.images import *

df=pd.read_csv('diabetes.csv')

root = tk.Tk()

canvas = tk.Canvas(root, width=1000, height=600)
canvas.grid(columnspan=5, rowspan=3)

logo('tkinter_gui/images/logo.png')

root.mainloop()

