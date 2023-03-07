from datetime import date
from tkinter import Toplevel, Tk, Canvas, Label, Text, Button
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
        mkdir_if_not_exists("./logs")
        self.logger = make_logger(
            logging_path="./logs/gui.log", logger_name="create-account"
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
        self.username = username_textbox
        username_textbox.grid(row=row_count, column=1)

        row_count += 1
        # Insert password label
        password_label = Label(self, text="Password:")
        password_label.grid(row=row_count, column=0)

        # Insert password textbox
        password_textbox = Text(self, height=1, width=20)
        self.password = password_textbox
        password_textbox.grid(row=row_count, column=1)

        row_count += 1
        # Insert email label
        email_label = Label(self, text="Email:")
        email_label.grid(row=row_count, column=0)

        # Insert email textbox
        email_textbox = Text(self, height=1, width=20)
        self.email = email_textbox
        email_textbox.grid(row=row_count, column=1)

        row_count += 1
        # Ins first name label
        first_name_label = Label(self, text="First name:")
        first_name_label.grid(row=row_count, column=0)

        # Ins first name textbox
        first_name_textbox = Text(self, height=1, width=20)
        self.first_name = first_name_textbox
        first_name_textbox.grid(row=row_count, column=1)

        row_count += 1
        # Ins last name label
        last_name_label = Label(self, text="Last name:")
        last_name_label.grid(row=row_count, column=0)

        # Ins last name textbox
        last_name_textbox = Text(self, height=1, width=20)
        self.last_name = last_name_textbox
        last_name_textbox.grid(row=row_count, column=1)

        row_count += 1
        # Insert DOB label
        dob = Label(self, text="Date of birth:")
        dob.grid(row=row_count, column=0)

        # insert calendar element
        dob_entry = DateEntry(self)
        self.dob = dob_entry
        dob_entry.grid(row=row_count, column=1)

        row_count += 1
        # Insert height label
        height_label = Label(self, text="Height (cm):")
        height_label.grid(row=row_count, column=0)

        # Insert height textbox
        height_textbox = Text(self, height=1, width=20)
        self.height = height_textbox
        height_textbox.grid(row=row_count, column=1)

        row_count += 1
        # Insert weight label
        weight_label = Label(self, text="Weight (kg):")
        weight_label.grid(row=row_count, column=0)

        # Insert weight textbox
        weight_textbox = Text(self, height=1, width=20)
        self.weight = weight_textbox
        weight_textbox.grid(row=row_count, column=1)

        row_count += 1
        # Insert submit button
        create_account_button = Button(
            self, text="create account", command=self.create_user
        )
        create_account_button.grid(row=row_count, column=1)

        row_count += 1
        # Denial label
        denial_label = Label(self, text="", pady=5, padx=5)
        self.denial_label = denial_label
        denial_label.grid(row=row_count, column=1)

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

    def __insert_user(
        self,
        username: str,
        password: str,
        email: str,
        first_name: str,
        last_name: str,
        dob,
        height: float,
        weight: float,
    ):
        insert_statement = f"""
        INSERT INTO 
            users (username,password,email,first_name,last_name,"DOB",height,weight)
        VALUES
            ('{username}','{password}','{email}','{first_name}','{last_name}','{dob}'::DATE,{height},{weight})
        """
        validation.sql_client.execute_create(insert_statement)

    def create_user(self):
        username = self.username.get(1.0, "end-1c")
        password = self.password.get(1.0, "end-1c")
        email = self.email.get(1.0, "end-1c")
        first_name = self.first_name.get(1.0, "end-1c")
        last_name = self.last_name.get(1.0, "end-1c")
        dob = self.dob.get_date()
        height = self.height.get(1.0, "end-1c")
        weight = self.weight.get(1.0, "end-1c")
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
                first name: {first_name}
                last name: {last_name}
                date of birth: {dob}
                height: {height}
                weight: {weight}
            """
            )
            self.__insert_user(
                username, password, email, first_name, last_name, dob, height, weight
            )
            # Close window on successful register
            self.destroy()
        else:
            self.logger.error(
                f"""
            Could NOT create user with:
                username: {username}
                password: {password}
                email: {email}
                height:{height}
                date of birth:{dob}
            """
            )
            self.denial_label.config(text="username,password or email is taken")
