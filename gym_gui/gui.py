from tkinter import *

from PIL import Image, ImageTk

root = Tk()  # create the base container

# Canvas
canvas = Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)  # Can make a grid

# Logo
logo = Image.open("gym_gui/images/barbell.png")
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Instructions
instructions = Label(root, text="Press the button below!", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

root.mainloop()
