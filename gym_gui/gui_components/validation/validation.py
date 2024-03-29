from typing import Dict

from gui_components.config.postgres_config import postgres_authentication

from get_utilities import utilities

from utilities.sql.sql_wrapper import Sql_wrapper
from utilities.logging.make_logger import make_logger
from utilities.utility.os_utilities import mkdir_if_not_exists


class Validate_input:
    def __init__(self, authentication: dict = postgres_authentication) -> None:
        self.authentication = authentication
        self.sql_client = Sql_wrapper(*list(postgres_authentication.values()))

        # Make logger
        mkdir_if_not_exists("./logs")
        self.logger = make_logger(
            logging_path="./logs/gui.log", logger_name="validator"
        )

    def __make_response_body(self, response: str, response_code: int) -> Dict[str, str]:
        return {"response": response, "response_code": response_code}

    def validate_user_password(self, username: str, password: str) -> Dict[str, str]:
        user_password_check_query = f"""
            SELECT
                *
            FROM
                users
            WHERE 
                username = '{username}' 
                AND 
                password = '{password}'"""

        user_password_check_result = self.sql_client.execute_read(
            user_password_check_query
        )

        user_password_check_result.pop(
            0
        )  # First element is always the column names, thus we remove it to check if query is truly empty

        if user_password_check_result != []:
            response = self.__make_response_body("authentication successful", 200)
            self.logger.info(response)
            return response
        else:
            response = self.__make_response_body("authentication unsuccessful", 400)
            self.logger.error(response)
            return response

    def available_field(self, field: str, username: str) -> Dict[str, str]:
        available_field_query = f"""
        SELECT 
            *
        FROM
            users
        WHERE {field} = '{username}'
        """

        available_field_query_result = self.sql_client.execute_read(
            available_field_query
        )
        available_field_query_result.pop(0)  # Remove columns

        if not available_field_query_result:
            response = self.__make_response_body(f"{field} available", 200)
            self.logger.info(response)
            return response
        response = self.__make_response_body(f"{field} unavailable", 400)
        self.logger.error(response)
        return response
