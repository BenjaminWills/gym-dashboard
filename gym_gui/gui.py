from tkinter import Tk

from gui_components.home_window import Home_window
from gui_components.login import Login_window

root = Tk()  # create the base container
root.geometry("+%d+%d" % (350, 40))  # Window placement

Login_window(root)

root.mainloop()
