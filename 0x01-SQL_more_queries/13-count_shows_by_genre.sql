-- list all genres from hbtn_0d_tvshows and display number of shows linked
-- to each. Each record should display:
-- <TV Show genre> - <Number of shows linked to this genre>
-- first column called 'genre', second called 'number_of_shows'
-- skip genres without any shows linked
-- sort by descending order of # shows linked
-- only use one SELECT statement
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id ORDER BY number_shows DESC;
