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
    db_name=args.db_name,
)

print(sql.db_name)
