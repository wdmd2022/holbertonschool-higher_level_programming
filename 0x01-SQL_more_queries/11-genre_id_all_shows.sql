-- using that same database dump as before, list all shows in the db
-- each record should display <tv_shows.title> - <tv_show_genres.genre_id>
-- results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- only use SELECT once
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
