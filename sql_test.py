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
            password VARCHAR(20)
        );"""

table_insertion_query = """
INSERT INTO 
    users (username,password)
VALUES
    ('test_user','test_password')
"""
t = "test_user"
p = "test_password"
if __name__ == "__main__":
    # sql.execute_create(table_creation_query)
    # sql.execute_create(table_insertion_query)
    print(sql.execute_read("SELECT * FROM users"))
    print(
        sql.execute_read(
            f"""
    SELECT
        *
    FROM
        users
    WHERE
        username = '{t}' 
        AND 
        password = '{p}'
    """
        )
    )
