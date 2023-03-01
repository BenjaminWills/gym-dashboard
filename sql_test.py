from utilities.sql.sql_wrapper import Sql_wrapper


sql = Sql_wrapper(
    username="admin",
    password="password",
    host="localhost",
    port=5432,
    db_name="gym_application",
)

if __name__ == "__main__":
    sql.execute_create("CREATE TABLE test(t INT);")
    sql.execute_create("INSERT INTO test VALUES (1);")
    print(sql.execute_read("SELECT * FROM test;"))
