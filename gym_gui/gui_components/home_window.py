from tkinter import Tk, Canvas, Label, Button, StringVar, Text, Entry
from tkinter.filedialog import askopenfile

from PIL import Image, ImageTk


class Home_window:
    def __init__(self, master_root: Tk) -> None:
        self.root = master_root

        # Canvas
        canvas = Canvas(self.root, width=600, height=300)
        canvas.grid(columnspan=3, rowspan=3)  # Can make a grid

        # Logo
        logo = Image.open("gym_gui/images/barbell.png")
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(image=logo)
        logo_label.image = logo
        logo_label.grid(column=0, row=0)

        # Browse button
        self.browse_text = StringVar()
        browse_btn = Button(
            self.root,
            textvariable=self.browse_text,
            command=lambda: self.open_file(),
            font="Raleway",
            bg="#808080",
            fg="black",
            height=2,
            width=15,
        )
        self.browse_text.set("Select file...")
        browse_btn.grid(column=1, row=0)

        # Entry box
        entry = Entry(self.root)
        entry.grid(column=1, row=1)

        # Add additional depth
        canvas = Canvas(self.root, width=600, height=250)
        canvas.grid(columnspan=3)

    def open_file(self):
        self.browse_text.set("loading...")

        file = askopenfile(parent=self.root, mode="rb", title="Choose a file!")
        if file:

            # Textbox

            text_box = Text(self.root, height=10, width=50, padx=15, pady=15)
            text_box.insert(1.0, file.name)
            text_box.tag_configure("center", justify="center")
            text_box.tag_add("center", 1.0, "end")
            text_box.grid(column=1, row=3)

            self.browse_text.set("Select file...")
