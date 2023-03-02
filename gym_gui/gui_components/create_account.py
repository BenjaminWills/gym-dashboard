from tkinter import Toplevel, Tk, Canvas, Label, Text
from tkcalendar import DateEntry

from gui_components.validation.validation import Validate_input
from get_utilities import utilities

from utilities.logging.make_logger import make_logger
from utilities.utility.os_utilities import mkdir_if_not_exists

validation = Validate_input()


class Create_account(Toplevel):
    def __init__(self, master_root: Tk) -> None:

        super().__init__(master=master_root)
        self.title("create account")

        # Make logger
        mkdir_if_not_exists("./log")
        self.logger = make_logger(
            logging_path="./log/gui.log", logger_name="create-account"
        )

        # Create a canvas
        canvas = Canvas(self, width=300, height=300)
        canvas.grid(columnspan=3, rowspan=8)

        row_count = 0
        # Insert title label
        title = Label(self, text="Create an account:")
        title.grid(row=row_count, column=0, columnspan=3)

        row_count += 1
        # Insert username label
        username_label = Label(self, text="Username:")
        username_label.grid(row=row_count, column=0)

        # Insert username textbox
        username_textbox = Text(self, height=1, width=20)
        username_textbox.grid(row=row_count, column=1)

        row_count += 1
        # Insert password label
        password_label = Label(self, text="Password:")
        password_label.grid(row=row_count, column=0)

        # Insert password textbox
        password_textbox = Text(self, height=1, width=20)
        password_textbox.grid(row=row_count, column=1)

        row_count += 1
        # Insert email label
        email_label = Label(self, text="Email:")
        email_label.grid(row=row_count, column=0)

        # Insert email textbox
        email_textbox = Text(self, height=1, width=20)
        email_textbox.grid(row=row_count, column=1)

        row_count += 1
        # Insert height label
        height_label = Label(self, text="Height:")
        height_label.grid(row=row_count, column=0)

        # Insert height textbox
        height_textbox = Text(self, height=1, width=20)
        height_textbox.grid(row=row_count, column=1)

        row_count += 1
        # Insert DOB label
        dob = Label(self, text="Date of birth:")
        dob.grid(row=row_count, column=0)

        # insert calendar element
        dob_entry = DateEntry(self)
        dob_entry.grid(row=row_count, column=1)

    def __validate_user(self, username: str) -> int:
        return validation.available_field("username", username).get(
            "response_code", 400
        )

    def __validate_pass(self, password: str) -> int:
        return validation.available_field("password", password).get(
            "response_code", 400
        )

    def __validate_email(self, email: str) -> int:
        return validation.available_field("email", email).get("response_code", 400)

    def create_user(self):
        username = ""
        password = ""
        email = ""
        if (
            self.__validate_email(email) == 200
            and self.__validate_pass(password) == 200
            and self.__validate_user(username) == 200
        ):
            self.logger.info(
                f"""
            Created user with:
                username: {username}
                password: {password}
                email: {email}
            """
            )
            pass
