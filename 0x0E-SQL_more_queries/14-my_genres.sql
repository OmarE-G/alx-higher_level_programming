-- Genres
SELECT name FROM tv_genres JOIN
   (tv_shows JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id)
   ON tv_genres.id = genre_id
 WHERE title='Dexter'
 ORDER BY name;
