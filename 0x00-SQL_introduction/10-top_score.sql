-- list all records of the table second_table in the
-- db hbtn_0c_0 with results displaying the top score and the name
-- (in this order) and with the records ordered by score (top first)
SELECT `score`, `name`
FROM second_table 
ORDER BY `score` DESC;
