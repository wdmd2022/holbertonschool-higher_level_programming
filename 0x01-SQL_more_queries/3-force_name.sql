-- create a table called force_name with id (INT) and name (VARCHAR(256)),
-- can't be null. If the table already exists, script should not fail
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
