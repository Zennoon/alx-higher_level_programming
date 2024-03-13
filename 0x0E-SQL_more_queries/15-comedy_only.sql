-- Displays all Comedy shows in the database
SELECT tv_shows.title AS title
  FROM tv_genres
       INNER JOIN tv_show_genres
       ON tv_genres.id = tv_show_genres.genre_id
       AND tv_genres.name = 'Comedy'

       INNER JOIN tv_shows
       ON tv_show_genres.show_id = tv_shows.id
 ORDER BY title;
