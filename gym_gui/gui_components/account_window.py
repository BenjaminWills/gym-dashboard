from tkinter import Toplevel, Tk, Button, Canvas

from gym_gui.gui_components.query import Query


class Account_home(Toplevel):
    def __init__(self, master_root: Tk):

        self.root = master_root

        super().__init__(master_root)
        self.title("query page")

        # Canvas
        canvas = Canvas(self, width=300, height=450)
        canvas.grid(columnspan=3, rowspan=6)

        # Execute query button
        execute_query_button = Button(
            self, text="Query the database", command=self.execute
        )
        execute_query_button.grid(row=2, column=1)

    def execute(self):
        Query(self.root)
