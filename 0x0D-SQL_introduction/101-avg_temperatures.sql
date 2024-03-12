-- Displays average temperature by City of the temperature table in hbtn_0c_0
SELECT city, AVG(value) AS avg_tmp FROM temperatures GROUP BY city ORDER BY AVG(value) DESC;
