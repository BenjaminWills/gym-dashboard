CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(20),
    password VARCHAR(20)
);

INSERT INTO users (username,password) VALUES ('user','pass');