import sqlalchemy
import psycopg2

# with psycopg2.connect("postgres://docker:docker@localhost:5432/exampledb") as conn:
#     with conn.cursor() as cur:
#         cur.execute("SELECT * FROM test")
#         rows = cur.fetchall()

# if not rows:
#     print("DEY DONT EXIST")
# else:
#     for row in rows:
#         print(row)

engine = sqlalchemy.create_engine(
    "postgresql+psycopg2://docker:docker@localhost:5432/exampledb"
)

with engine.connect() as connection:
    result = connection.execute(sqlalchemy.text("SELECT * FROM test"))
    for row in result:
        print(row)
