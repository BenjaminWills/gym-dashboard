from tkinter import Toplevel, Tk, Canvas


class Add_workout(Toplevel):
    def __init__(self, master_root: Tk):
        self.root = master_root

        super().__init__(master_root)
        self.title("Add a workout")

        # Canvas
        canvas = Canvas(self, width=300, height=450)
        canvas.grid(columnspan=3, rowspan=6)
