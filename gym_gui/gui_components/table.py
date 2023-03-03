import csv

from tkinter import (
    Toplevel,
    Tk,
    Entry,
    END,
    Button,
    ttk,
    Frame,
    BOTH,
    LEFT,
    Canvas,
    RIGHT,
)
from tkinter.filedialog import asksaveasfile

from gui_components.validation.validation import Validate_input

v = Validate_input()


class Query_table(Toplevel):
    def __init__(self, master_root: Tk, query: str) -> None:
        super().__init__(master=master_root)

        # Window title
        self.title("Query output")

        # Read query
        self.query_result = v.sql_client.execute_read(query)

        # Create frame
        query_frame = Frame(self)
        query_frame.pack(fill=BOTH, expand=1)

        # Create a Canvas
        query_canvas = Canvas(query_frame)
        query_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add a scrollbar to the canvas
        scrollbar = ttk.Scrollbar(
            query_frame, orient="vertical", command=query_canvas.yview
        )
        scrollbar.pack(side=RIGHT, fill="y")

        # Configure the canvas
        query_canvas.configure(yscrollcommand=scrollbar.set)
        query_canvas.bind(
            "<Configure>",
            lambda e: query_canvas.configure(scrollregion=query_canvas.bbox("all")),
        )  # Config scroll on click

        # Create other frame within query frame
        second_frame = Frame(query_canvas)
        self.second_frame = second_frame

        # Add second frame to a window in the canvas
        query_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        # Format and create table
        self.total_columns = len(self.query_result[0])
        self.total_rows = len(self.query_result)

        for column in range(self.total_columns):
            for row in range(self.total_rows):
                if row == 0:
                    self.e = Entry(
                        second_frame, width=20, fg="black", font=("Arial", 16, "bold")
                    )
                else:
                    self.e = Entry(
                        second_frame, width=20, fg="blue", font=("Arial", 16, "bold")
                    )
                self.e.grid(row=row, column=column)
                self.e.insert(END, self.query_result[row][column])

        # Save output to csv button
        save_csv_button = Button(
            second_frame, text="Save as CSV", command=self.save_output_as_csv
        )
        save_csv_button.grid(row=self.total_rows + 1, columnspan=2, column=0)

    def save_output_as_csv(self):
        file = asksaveasfile(
            parent=self.second_frame, initialfile="query", defaultextension=".csv"
        )
        if file:
            file_path = file.name

            with open(file_path, mode="w") as outfile:
                writer = csv.writer(outfile, delimiter=",")
                for row in self.query_result:
                    writer.writerow(row)
