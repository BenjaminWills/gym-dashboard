from tkinter import Toplevel, Tk


class Create_account(Toplevel):
    def __init__(self, master_root: Tk) -> None:

        super().__init__(master=master_root)
        self.title("create account")
