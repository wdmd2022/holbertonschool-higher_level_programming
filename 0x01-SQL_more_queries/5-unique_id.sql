-- create table unique_id on our MySQL server. Has id, an int (default 1)
-- that's unique, name (VARCHAR(256)), anf shouldn't fail if already exists
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
