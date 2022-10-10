-- list the number of records with the same score in second_table
-- result should display score, number of records w/ given score labeled 'number'
-- sort descending
SELECT score, COUNT(*) as number FROM second_table
GROUP BY score ORDER BY number DESC;
