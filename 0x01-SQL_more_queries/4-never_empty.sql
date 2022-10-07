-- create the table id_not_null on our MySQL server
-- with id (INT, default value = 1) and name (VARCHAR(256))
-- if the table already exists, you must not fail
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
