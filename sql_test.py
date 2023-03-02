from utilities.sql.sql_wrapper import Sql_wrapper


sql = Sql_wrapper(
    username="admin",
    password="password",
    host="localhost",
    port=5432,
    db_name="gym_application",
)

table_creation_query = """
    CREATE TABLE IF NOT EXISTS 
        users(
            id SERIAL PRIMARY KEY,
            username VARCHAR(20),
            password VARCHAR(20),
            email VARCHAR(20),
            height FLOAT,
            dob DATE
        );"""

table_insertion_query = """
INSERT INTO 
    users (username,password,email,height,dob)
VALUES
    ('test_user','test_password','email@email.com',181,'07-03-2001'::date)
"""
t = "test_user"
p = "test_password"
if __name__ == "__main__":
    # sql.execute_create("DELETE FROM users")
    # sql.execute_create("DROP TABLE users")
    # sql.execute_create(table_creation_query)
    # sql.execute_create(table_insertion_query)
    print(sql.execute_read("SELECT * FROM users"))
