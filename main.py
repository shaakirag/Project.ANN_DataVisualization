from tkinter_gui.funcs import *
from tkinter_gui.images import *
from tkinter_gui.images.images import *
from tkinter.ttk import *

HEIGHT = 1000
WIDTH = 700

font = 'Raleway'

root = tk.Tk()
root.geometry("600x600")

#canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
#canvas.pack()

main_notebook = Notebook(root)
main_notebook.pack(pady=15)

# Welcome Page

# Does not work
# set_background(root, 'tkinter_gui/images/background.png')

frame = tk.Frame(main_notebook, bg='White', width=600, height=600, bd=5)
#frame.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.9)
frame.pack(fill='both', expand=1)

main_notebook.add(frame, text='Home')

set_logo(frame, 'tkinter_gui/images/logo.png')

# Menu
menubar = tk.Menu(main_notebook)
filemenu = tk.Menu(menubar, tearoff=0)
editmenu = tk.Menu(menubar, tearoff=0)

root.config(menu=menubar)

# Instructions message
instructions_txt = tk.StringVar()
instructions_btn = tk.Button(frame, textvariable=instructions_txt, command=lambda: instructions(main_notebook, font), font=font,
                             bg='White', fg='Black', height=2, width=15)
instructions_txt.set('Instructions')
instructions_btn.place(relx=0.325, rely=0.7, relwidth=0.35, relheight=0.05)

# Browse button
browse_txt = tk.StringVar()
browse_btn = tk.Button(frame, textvariable=browse_txt,
                       command=lambda: open_file(main_notebook, frame, menubar, filemenu, editmenu, browse_txt, False, font), font=font,
                       bg='#008080', fg='White', height=2, width=15)
browse_txt.set('Browse')
# browse_btn.grid(column=2, row=3)
browse_btn.place(relx=0.425, rely=0.77, relwidth=0.15, relheight=0.05)

close = tk.Button(main_notebook, text='Close', command=root.destroy, font=font, bg='Black', fg='White')
close.place(relx=0.45, rely=0.95, relwidth=0.1, relheight=0.04)

root.mainloop()
