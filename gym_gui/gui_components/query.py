from tkinter import Toplevel, Tk, Text, Canvas, Label, Button, ttk

from gui_components.table import Query_table


class Query(Toplevel):
    def __init__(self, master_root: Tk):

        self.root = master_root

        super().__init__(master_root)
        self.title("query page")

        # Canvas
        canvas = Canvas(self, width=300, height=450)
        canvas.grid(columnspan=3, rowspan=6)

        # Insert query label
        query_label = Label(self, text="Query:")
        query_label.grid(row=0, column=0, columnspan=3)

        # Insert query textbox
        query_textbox = Text(self, height=10, width=50, wrap="none")
        query_textbox.grid(row=1, column=1, sticky="nwes")
        self.query = query_textbox

        # Add vertical scroller
        ys = ttk.Scrollbar(self, orient="vertical", command=query_textbox.yview)
        query_textbox["yscrollcommand"] = ys.set
        ys.grid(row=1, column=2, sticky="ns")

        # Execute query button
        execute_query_button = Button(self, text="Execute SQL", command=self.execute)
        execute_query_button.grid(row=2, column=1)

    def execute(self):
        text = self.query.get(1.0, "end-1c")
        Query_table(self.root, text)
