-- Displays  all genres from a database and displays the number of shows
-- linked to each
SELECT tv_genres.name AS genre, COUNT(tv_genres.id) AS number_of_shows
  FROM tv_shows
       INNER JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id

       INNER JOIN tv_genres
       ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
