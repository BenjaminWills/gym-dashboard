from utilities.sql.sql_wrapper import Sql_wrapper


sql = Sql_wrapper(
    username="postgres",
    password="postgres",
    host="postgres",
    port=5432,
    db_name="gym_tracker",
)

if __name__ == "__main__":
    print(sql.execute_query("SELECT * FROM test"))
