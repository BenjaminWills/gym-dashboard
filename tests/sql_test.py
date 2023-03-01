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
    "CREATE DATABASE test_db",
    "CREATE TABLE test_db.test_table(id INT,name VARCHAR)",
    "INSERT INTO test_db.test_table (1,'ben')",
]

for query in queries:
    sql.execute_query(query)

print(sql.execute_query("select * from test_table"))
