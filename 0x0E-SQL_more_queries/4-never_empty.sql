-- Creates a table if it doesn't exist in a database whose name is passed as
-- an arg.
CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT 1,
       name VARCHAR(256)
);
