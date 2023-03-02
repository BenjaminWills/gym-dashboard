from gui_components.config.postgres_config import postgres_authentication

from get_utilities import utilities

from utilities.sql.sql_wrapper import Sql_wrapper


class Validate_input:
    def __init__(self, authentication: dict = postgres_authentication) -> None:
        self.authentication = authentication
        self.sql_client = Sql_wrapper(*list(postgres_authentication.values()))

    def __make_response_body(self, response: str, response_code: int):
        return {"response": response, "response_code": response_code}

    def validate_user_password(self, username: str, password: str) -> int:
        if self.sql_client.execute_read(
            f"""
            SELECT
                *
            FROM
                users
            WHERE 
                username = '{username}' 
                AND 
                password = '{password}'"""
        ):
            return self.__make_response_body("authentication successful", 200)
        return self.__make_response_body("authentication unsuccessful", 400)
