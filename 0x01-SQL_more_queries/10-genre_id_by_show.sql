-- import a database dump called hbtn_0d_tvshows to your MySQL server, then
-- list all shows contained in it that have at least one genre linked
-- each record should display <tv_shows.title> <tv_show_genres.genre_id>
-- sort in ascending order by tv_shows.title and tv_show_genres.genre_id
-- use only one SELECT command
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
