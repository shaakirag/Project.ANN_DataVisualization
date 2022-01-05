from PIL import Image, ImageTk
import tkinter as tk

def set_logo(frame, image):
    logo = Image.open(image)
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(frame, image=logo)
    logo_label.image = logo
    logo_label.place(relx=0.225, rely=0.1, relwidth=0.55, relheight=0.55)

def set_background(root, image):
    background = tk.PhotoImage(image)
    background_label = tk.Label(root, image=background)
    background_label.place(relx=0, rely=0, relwidth=1, relheight=1)