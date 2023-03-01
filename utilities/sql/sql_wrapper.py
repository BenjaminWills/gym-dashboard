import pandas as pd
import sqlalchemy as SQLA
from sqlalchemy import text

from utilities.logging.make_logger import make_logger
from utilities.utility.os_utilities import mkdir_if_not_exists


class Sql_wrapper:

    """
    Wrapper for sqlalchemy to query a postgresql db.
    """

    def __init__(
        self, username: str, password: str, host: str, port: str, db_name: str
    ):

        self.engine = self.__make_engine(username, password, host, port, db_name)

        self.db_name = db_name

        # Make `postgresql` logger
        mkdir_if_not_exists("./logs")
        self.logger = make_logger(
            logging_path="./logs/postgresql.log", logger_name="postgres"
        )

    def __make_engine(
        self, username: str, password: str, host: str, port: str, db_name: str
    ):
        connection_string = (
            f"postgresql://{username}:{password}@{host}:{port}/{db_name}"
        )
        try:
            return SQLA.create_engine(connection_string)
        except Exception as e:
            print(e.with_traceback())

    def execute_query(self, query: str) -> pd.DataFrame:
        """Will execute a query against a selected table.

        Parameters
        ----------
        query : str
            A string containing the query to be executed.

        Returns
        -------
        pd.DataFrame
            Pandas data frame containing query output.
        """
        try:
            self.logger.info(
                f"""
            Executing query on database: {self.db_name}:
                {query}
            """
            )
            with self.engine.connect() as con:
                results = con.execute(text(query))
                returns = results.fetchall()
            self.logger.info(f"Query sucessfully executed and returned \n {results}")
            return returns
        except Exception as e:
            self.logger.error("Query failed with stacktrace: ")
            self.logger.error(e)

    def input_data(self, data: tuple, table: str):

        con = self.engine()
        try:
            con.execute(
                f"""
            INSERT INTO {table} VALUES
            {data};
            """
            )
            return f"Inputting successful into table"
        except:
            return "Insertion failed."
        finally:
            con.close()
