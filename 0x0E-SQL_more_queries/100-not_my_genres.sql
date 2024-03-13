-- Displays all the genres that are not linked to the show 'Dexter'
SELECT tv_genres.name
  FROM tv_genres

EXCEPT

SELECT tv_genres.name
  FROM tv_shows
       INNER JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
       AND tv_shows.title = 'Dexter'

       INNER JOIN tv_genres
       ON tv_show_genres.genre_id = tv_genres.id
 ORDER BY name
