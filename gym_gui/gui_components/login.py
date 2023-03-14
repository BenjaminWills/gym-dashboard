from tkinter import Tk, Canvas, Label, Text, Button, Entry
from PIL import Image, ImageTk

from gui_components.validation.validation import Validate_input
from gui_components.create_account import Create_account
from gui_components.query import Query
from gui_components.account_window import Account_home


class Login_window:
    def __init__(self, master_root: Tk) -> None:

        self.root = master_root

        self.root.title("login")
        # Canvas
        canvas = Canvas(self.root, width=300, height=450)
        canvas.grid(columnspan=3, rowspan=5)

        # Insert barbell logo
        logo = Image.open("gym_gui/images/barbell.png")
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
        password_textbox = Entry(width=10, show="*")
        self.password = password_textbox
        password_textbox.grid(row=2, column=1)

        # Insert submit button to send request to database
        submit_button = Button(text="Submit", command=self.submit)
        submit_button.grid(row=3, column=1)

        # Create account button
        create_account_button = Button(
            text="Create account", command=self.create_account
        )
        create_account_button.grid(row=5, column=1)

        # Test label
        response = Label(text="")
        self.response = response
        response.grid(row=4, column=1)

    def submit(self):
        user = self.username.get(1.0, "end-1c")
        password = self.password.get()
        validate = Validate_input()

        validation_result = validate.validate_user_password(user, password)
        if validation_result.get("response_code") == 200:
            self.response.config(text=f"Access granted")
            Account_home(self.root)
        else:
            self.response.config(text=f"Access denied")

    def create_account(self):
        Create_account(self.root)
