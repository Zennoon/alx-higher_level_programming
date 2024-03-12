-- Displays all records of a table whose name value is not empty/NULL
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
