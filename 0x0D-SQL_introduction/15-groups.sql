-- Displays the number of records for every distinct score in a table.
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score ORDER BY score DESC;
