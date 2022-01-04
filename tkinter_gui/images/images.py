from all_libs import *

def set_logo(image):
    logo = Image.open(image)
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    #logo_label.grid(column=2,row=0)
    logo_label.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.5)