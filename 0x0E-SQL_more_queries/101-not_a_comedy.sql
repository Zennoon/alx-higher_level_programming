-- Displays all shows without the genre Comedy.
SELECT tv_shows.title AS title
  FROM tv_shows
 WHERE tv_shows.id NOT IN
       (SELECT tv_shows.id
        FROM tv_genres
       	      INNER JOIN tv_show_genres
       	      ON tv_genres.id = tv_show_genres.genre_id
       	      AND tv_genres.name = 'Comedy'

	      INNER JOIN tv_shows
       	      ON tv_show_genres.show_id = tv_shows.id)
ORDER BY title;
