-- list all genres of the show Dexter from the same database
-- reach record should display tv_genres.name, sorted ascending
-- use only one SELECT statement. tv_shows table only contains 1 record
-- where title = Dexter, FYI
SELECT tv_genres.name FROM tv_genres INNER JOIN tv_show_genres
