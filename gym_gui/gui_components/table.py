from tkinter import Toplevel, Tk, Entry, END

from gui_components.validation.validation import Validate_input

v = Validate_input()


class Query_table(Toplevel):
    def __init__(self, master_root: Tk, query: str) -> None:
        super().__init__(master=master_root)
        self.title("create account")

        self.query_result = v.sql_client.execute_read(query)

        self.total_columns = len(self.query_result[0])
        self.total_rows = len(self.query_result)

        for column in range(self.total_columns):
            for row in range(self.total_rows):
                self.e = Entry(
                    master_root, width=20, fg="blue", font=("Arial", 16, "bold")
                )
                self.e.grid(row=row, column=column)
                self.e.insert(END, self.query_result[row][column])
