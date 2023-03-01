CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(20),
    password VARCHAR(20),
    age INT,
    birthday DATE,
    weight FLOAT,
    height FLOAT
);

INSERT INTO users VALUES ("test","test",2,"07-03-2001",78.0,1.81);