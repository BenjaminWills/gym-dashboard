import pandas as pd
import sqlalchemy as SQLA

from utilities.logging.make_logger import make_logger


class Sql_wrapper:
    
    """
    Wrapper for sqlalchemy to query a postgresql db.
    """

    def __init__(self,username:str,password:str,host:str,port:str,db_name:str):
        engine = SQLA.create_engine(f"postgresql://{username}:{password}@{host}:{port}/{db_name}")
        self.engine = engine

        # Make `postgresql` logger

        self.logger = make_logger(
            logging_path="./postgresql.log",
        )

    def execute_query(self,query:str) -> pd.DataFrame:
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
            self.logger.info(f"""
            Executing query:
                {query}
            """)
            with self.engine.connect() as con:
                results = con.execute(query)
                returns = results.fetchall()
            self.logger.info("Query sucessfully executed")
            return pd.DataFrame(returns)
        except:
            self.logger.error("Query failed")
        

    def input_data(self,data:tuple,table:str):
        
        con = self.engine()
        try:
            con.execute(f"""
            INSERT INTO {table} VALUES
            {data};
            """)
            return f"Inputting successful into table"
        except:
            return "Insertion failed."
        finally:
            con.close()