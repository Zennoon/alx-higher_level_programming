-- Creates a database and a table inside of it if they don't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
       PRIMARY KEY (id),
       id INT AUTO_INCREMENT,
       name VARCHAR(256) NOT NULL
);
