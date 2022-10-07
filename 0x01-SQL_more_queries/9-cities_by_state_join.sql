-- list all the cities contained in the database hbtn_0d_usa
-- do it in format <cities.id> <cities.name> <states.name>
-- sort in ascending order by cities.id
-- use only one SELECT statement -- go ahead, impress me
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
