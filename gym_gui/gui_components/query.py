from tkinter import Toplevel, Tk, Text, Canvas, Label, Button

from gui_components.table import Query_table


class Query(Toplevel):
    def __init__(self, master_root: Tk):

        self.root = master_root

        super().__init__(master_root)
        self.title("query page")

        # Canvas
        canvas = Canvas(self, width=300, height=450)
        canvas.grid(columnspan=3, rowspan=5)

        # Insert query label
        query_label = Label(self, text="Query:")
        query_label.grid(row=0, column=0, columnspan=3)

        # Insert query textbox
        query_textbox = Text(self, height=20, width=20)
        query_textbox.grid(row=1, column=1)
        self.query = query_textbox

        # Execute query button
        execute_query_button = Button(self, text="Execute SQL", command=self.execute)
        execute_query_button.grid(row=2, column=1)

    def execute(self):
        text = self.query.get(1.0, "end-1c")
        Query_table(self.root, text)
