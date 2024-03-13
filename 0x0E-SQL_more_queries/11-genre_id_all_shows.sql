-- Displays all tv shows in a database regardless of whether they are linked
-- to a genre or not.
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
  FROM tv_shows
       LEFT JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
 ORDER BY title, genre_id
