import sqlalchemy as SQLA
import pandas as pd

class Sql_wrapper:
    def __init__(self,username:str,password:str,host:str,port:str,db_name:str):
        engine = SQLA.create_engine(f"postgresql://{username}:{password}@{host}:{port}/{db_name}")
        self.engine = engine

    def execute_query(self,query:str) -> pd.DataFrame:
        """Will execute a query against a selected table.

        Parameters
        ----------
        query : str
            A string 

        Returns
        -------
        pd.DataFrame
            _description_
        """
        con = self.engine.connect()
        results = con.execute(query)
        returns = results.fetchall()
        con.close()
        return pd.DataFrame(returns)

