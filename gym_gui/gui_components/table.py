import csv

from tkinter import Toplevel, Tk, Entry, END, Button, ttk
from tkinter.filedialog import askopenfile

from gui_components.validation.validation import Validate_input

v = Validate_input()


class Query_table(Toplevel):
    def __init__(self, master_root: Tk, query: str) -> None:
        super().__init__(master=master_root)

        # Window title
        self.title("Query output")

        # Read query
        self.query_result = v.sql_client.execute_read(query)

        # Format and create table
        self.total_columns = len(self.query_result[0])
        self.total_rows = len(self.query_result)

        for column in range(self.total_columns):
            for row in range(self.total_rows):
                self.e = Entry(self, width=20, fg="blue", font=("Arial", 16, "bold"))
                self.e.grid(row=row, column=column)
                self.e.insert(END, self.query_result[row][column])

        # Save output to csv button
        save_csv_button = Button(text="Save as CSV", command=self.save_output_as_csv)
        save_csv_button.grid(row=self.total_rows + 1, columnspan=self.total_columns)

    def save_output_as_csv(self):
        pass
