from tkinter import Tk

from gui_components.home_window import Home_window

root = Tk()  # create the base container
root.geometry("+%d+%d" % (300, 40))  # Window placement

Home_window(root)

root.mainloop()
