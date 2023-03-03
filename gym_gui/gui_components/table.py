from tkinter import Toplevel, Tk, ttk, Scrollbar, Canvas

from gui_components.validation.validation import Validate_input

v = Validate_input()


class Query_table(Toplevel):
    def __init__(self, master_root: Tk, query: str) -> None:
        super().__init__(master=master_root)
        self.title("Query result")

        # Set geometry of window
        self.geometry("400x250")

        # Return query result
        self.query_result = v.sql_client.execute_read(query)
        self.columns = self.query_result[0]
        self.data = self.query_result[1:]

        # Rows and columns of query result
        rows = len(self.query_result)
        columns = len(self.query_result[0])

        # Initialise the tree
        tree_table = ttk.Treeview(self, selectmode="browse")
        tree_table.grid(row=4, column=1, columnspan=4, padx=5, pady=20)

        tree_table["height"] = 4
        tree_table["columns"] = self.columns
        tree_table["show"] = "headings"

        for column in self.columns:
            tree_table.column(column, anchor="c", width=70)
            tree_table.heading(column, text=column)
