from utilities.sql.sql_wrapper import Sql_wrapper


sql = Sql_wrapper(
    username="admin",
    password="password",
    host="localhost",
    port=5432,
    db_name="gym_application",
)

with open("postgres_server/init_gym_application.sql") as sql_document:
    sql_code = sql_document.read()

sql_code = sql_code.replace("\n", "")

creation_queries = sql_code.split(";")

if __name__ == "__main__":
    for query in creation_queries:
        sql.execute_create(query)
