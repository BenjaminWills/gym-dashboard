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
            A string containing the query to be executed.

        Returns
        -------
        pd.DataFrame
            Pandas data frame containing query output.
        """
        try:
            con = self.engine.connect()
            results = con.execute(query)
            returns = results.fetchall()
            return pd.DataFrame(returns)
        except:
            return "Query failed"
        finally:
            con.close()
        

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