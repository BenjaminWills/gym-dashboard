from utilities.sql.sql_wrapper import Sql_wrapper


sql = Sql_wrapper(
    username="docker",
    password="docker",
    host="localhost",
    port=5432,
    db_name="exampledb",
)

if __name__ == "__main__":
    print(sql.execute_query("SELECT * FROM test"))
