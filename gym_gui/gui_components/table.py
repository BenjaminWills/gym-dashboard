from tkinter import Toplevel, Tk, ttk, Scrollbar, Canvas

from gui_components.validation.validation import Validate_input

v = Validate_input()


class Query_table(Toplevel):
    def __init__(self, master_root: Tk, query: str) -> None:
        super().__init__(master=master_root)
        self.title("Query result")

        # Set geometry of window
        self.geometry("400x400")

        # Return query result
        self.query_result = v.sql_client.execute_read(query)
        self.columns = self.query_result[0]
        self.data = self.query_result[1:]

        # Rows and columns of query result
        rows = len(self.query_result)
        columns = len(self.query_result[0])

        # Initialise the tree
        tree_table = ttk.Treeview(
            self,
            selectmode="browse",
            columns=self.columns,
            height=rows,
            show="headings",
        )
        tree_table.grid(row=4, column=1, columnspan=4, padx=5, pady=20)

        # format tree columns
        tree_table.column("#0", width=120, minwidth=25)
        for column in self.columns:
            tree_table.column(column, anchor="c", width=70)
            tree_table.heading(column, text=column)

        for iid, row in enumerate(self.data):
            tree_table.insert("", "end", values=(1, 2, 3, 4, 5, 6), iid=iid)
