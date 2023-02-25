from tkinter import *

root = Tk()  # create the base container

label = Label(root, text="Hello World!")  # create a label widget
button = Button(root, text="Click me!", width=25, height=25, bg="blue", fg="yellow")

button.pack()
label.pack()  # places onto screen

root.mainloop()
