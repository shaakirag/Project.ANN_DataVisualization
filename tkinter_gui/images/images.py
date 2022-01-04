from all_libs import *

def set_logo(image):
    logo = Image.open(image)
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=2,row=0)
