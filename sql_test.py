from utilities.sql.sql_wrapper import Sql_wrapper


sql = Sql_wrapper(
    username="admin",
    password="password",
    host="localhost",
    port=5432,
    db_name="gym_application",
)

if __name__ == "__main__":
    print(sql.execute_read("SELECT * FROM users"))
