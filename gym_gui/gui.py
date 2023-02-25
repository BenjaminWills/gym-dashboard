from tkinter import *
from tkinter.filedialog import askopenfile

from PIL import Image, ImageTk

root = Tk()  # create the base container

# Canvas
canvas = Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)  # Can make a grid

# Logo
logo = Image.open("gym_gui/images/barbell.png")
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Instructions
instructions = Label(root, text="Press the button below!", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

# Browse function


def open_file():
    browse_text.set("loading...")

    file = askopenfile(parent=root, mode="rb", title="Choose a file!")

    if file:
        print(file.name)


# Browse button
browse_text = StringVar()
browse_btn = Button(
    root,
    textvariable=browse_text,
    command=lambda: open_file(),
    font="Raleway",
    bg="#808080",
    fg="black",
    height=2,
    width=15,
)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

# Add additional depth
canvas = Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()
