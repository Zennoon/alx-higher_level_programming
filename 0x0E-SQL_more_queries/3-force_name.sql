-- Creates a table if it doesn't exist in a database whose name is passed as
-- an arg.
CREATE TABLE IF NOT EXISTS force_name (
       id INT,
       name VARCHAR(256) NOT NULL
);
