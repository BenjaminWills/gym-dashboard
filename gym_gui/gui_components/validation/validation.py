from gui_components.config.postgres_config import postgres_authentication

from get_utilities import utilities

from utilities.sql.sql_wrapper import Sql_wrapper


class Validate_input:
    def __init__(self, authentication: dict = postgres_authentication) -> None:
        self.authentication = authentication
        self.sql_client = Sql_wrapper(*postgres_authentication.values)

    def validate_user_password(self, username: str, password: str) -> int:
        if self.sql_client.execute_query(
            f"SELECT * FROM users WHERE username = {username} AND password = {password}"
        ):
            return "authentication successful", 200
        return "authentication unsuccessful", 400
