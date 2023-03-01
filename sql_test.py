# from utilities.sql.sql_wrapper import Sql_wrapper


# sql = Sql_wrapper(
#     username="postgres",
#     password="postgres",
#     host="postgres",
#     port=5432,
#     db_name="gym_tracker",
# )

# if __name__ == "__main__":
#     print(sql.execute_query("SELECT * FROM test"))

import sqlalchemy

conn_string = "postgresql+psycopg2://admin:password@localhost:5432/gym_tracker"

engine = sqlalchemy.create_engine(conn_string)

with engine.connect() as conn:
    result = conn.execute("select * from test;")
    print(result.fetchall())
