-- list all the cities of Cali that can be found in the db hbtn_0d_usa
-- states table contains only one record where name = California (but the id can
-- be different). Sort results by ascending cities.id, don't use the JOIN command
SELECT id, name FROM cities
WHERE state_id = (SELECT id from states WHERE name = "California")
ORDER BY id;
