from tkinter import Toplevel, Tk, Button, Canvas, Label

from gym_gui.gui_components.query import Query

import json


class Account_home(Toplevel):
    def __init__(self, master_root: Tk, user_info: dict):

        self.root = master_root
        self.user_info = user_info

        super().__init__(master_root)
        self.title("query page")

        # Canvas
        canvas = Canvas(self, width=300, height=450)
        canvas.grid(columnspan=3, rowspan=6)

        row = 0
        # Display user info
        row = self.user_to_key_value_texboxes(row)

        row += 1
        # Execute query button
        execute_query_button = Button(
            self, text="Query the database", command=self.execute
        )
        execute_query_button.grid(row=row, column=1)

    def execute(self):
        Query(self.root)

    def user_to_key_value_texboxes(self, row: int):
        for key, value in self.user_info.items():
            key_label = Label(self, text=f"{key}:")
            key_label.grid(row=row, column=0)
            value_label = Label(self, text=f"{value}")
            value_label.grid(row=row, column=1)
            row += 1
        return row
