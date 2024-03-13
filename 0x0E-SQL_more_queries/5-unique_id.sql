-- Creates a table if it doesn't exist in a database whose name is passed as
-- an arg. The id field is given the UNIQUE constraint and has a default value 1
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
