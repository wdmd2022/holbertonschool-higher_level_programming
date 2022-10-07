-- create a table second_table in hbtn_0c_0 and add multiple rows
-- second_table should have: id (INT), name (VARCHAR(256)), score (INT)
-- if it exists already, script should not fail
-- can't use SELECT or SHOW statements
-- need to create 4 specific records
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, 'John', 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, 'Alex', 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, 'Bob', 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, 'George', 8);
