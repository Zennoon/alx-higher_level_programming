-- Displays the top 3 of cities temperatures during July and August
-- ordered by descending temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month = 7 OR month = 8 GROUP BY city ORDER BY AVG(value) DESC LIMIT 3;
