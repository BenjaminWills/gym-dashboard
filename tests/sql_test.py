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

sql.execute_query(
    """

CREATE DATABASE test_db;

USING test_db;

CREATE TABLE test_table(
    id INT,
    name VARCHAR
);

INSERT INTO test_table (1,"ben");
"""
)

print(sql.execute_query("select * from test_table"))
