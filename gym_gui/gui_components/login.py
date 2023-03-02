from tkinter import Tk, Canvas, Label, Text, Button, Frame
from PIL import Image, ImageTk

from gui_components.validation.validation import Validate_input


class Login_window:
    def __init__(self, master_root: Tk) -> None:

        self.root = master_root

        # Canvas
        canvas = Canvas(self.root, width=300, height=450)
        canvas.grid(columnspan=3, rowspan=4)

        # Insert barbell logo
        logo = Image.open("images/barbell.png")
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(image=logo)
        logo_label.image = logo
        logo_label.grid(column=1, row=0)

        # Insert username label
        username_label = Label(text="Username:")
        username_label.grid(row=1, column=0)

        # Insert textbox by username
        username_textbox = Text(height=1, width=20)
        username_textbox.grid(row=1, column=1)
        self.username = username_textbox

        # Insert password label
        password_label = Label(text="Password:")
        password_label.grid(row=2, column=0)

        # Insert textbox by password
        password_textbox = Text(height=1, width=20)
        self.password = password_textbox
        password_textbox.grid(row=2, column=1)

        # Insert submit button to send request to database
        submit_button = Button(text="Submit", command=self.submit)
        submit_button.grid(row=3, column=1)

        # Test label
        test = Label(text="")
        self.test = test
        test.grid(row=4, column=1)

    def submit(self):
        user = self.username.get(1.0, "end-1c")
        password = self.password.get(1.0, "end-1c")
        user_pass_dict = {"username": user, "password": password}
        self.test.config(text=f"{user_pass_dict}")

        validate = Validate_input()

        validation_result = validate.validate_user_password(user, password)
        print(validation_result)
        if validation_result.get("response_code") == 200:
            self.test.config(text=f"{user_pass_dict}")
        else:
            self.test.config(text=f"ACCESS DENIED")


if __name__ == "__main__":
    root = Tk()  # create the base container
    root.geometry("+%d+%d" % (350, 40))  # Window placement
    l = Login_window(root)

    root.mainloop()
