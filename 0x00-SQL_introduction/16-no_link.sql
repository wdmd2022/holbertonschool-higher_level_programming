-- list all records of the table second_table in your db
-- don't list rows without a name value
-- display results by score and name
-- list results by descending score
SELECT `score`, `name` FROM second_table WHERE `name` !=""
ORDER BY `score` DESC; 
