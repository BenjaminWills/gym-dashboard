from get_utilities import utilities

from utilities.sql.sql_wrapper import Sql_wrapper

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--username")
parser.add_argument("--password")
parser.add_argument("--host")
parser.add_argument("--port")
parser.add_argument("--db_name")

args = parser.parse_args()


sql = Sql_wrapper(
    username=args.username,
    password=args.password,
    host=args.host,
    port=args.port,
    db_name="",
)

queries = [
    """
    CREATE TABLE IF NOT EXISTS test_table(
    id SERIAL PRIMARY KEY,
    username VARCHAR(20),
    password VARCHAR(20)
    );
    """,
    "INSERT INTO test_table (username,password) VALUES ('user','pass');",
]

for query in queries:
    sql.execute_create(query)

print(sql.execute_read("select * from test_table"))
