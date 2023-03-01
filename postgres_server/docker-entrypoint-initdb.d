-- Initialise DB

CREATE DATABASE IF NOT EXISTS gym_application;

-- Initialise table

CREATE TABLE IF NOT EXISTS users(
    username VARCHAR(40) NOT NULL DEFAULT "user",
    password VARCHAR(40) NOT NULL DEFAULT "password"
)

INSERT INTO users VALUES("ben","password")