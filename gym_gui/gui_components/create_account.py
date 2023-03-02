from tkinter import Toplevel, Tk, Canvas, Label
from tkcalendar import DateEntry


class Create_account(Toplevel):
    def __init__(self, master_root: Tk) -> None:

        super().__init__(master=master_root)
        self.title("create account")

        # Create a canvas
        canvas = Canvas(self, width=300, height=300)
        canvas.grid(columnspan=3, rowspan=3)

        # Insert title label
        title = Label(self, text="Create an account:")
        title.grid(row=0, column=0, columnspan=3)

        # insert calendar element
        cal = DateEntry(self)
        cal.grid(row=2, column=1)
