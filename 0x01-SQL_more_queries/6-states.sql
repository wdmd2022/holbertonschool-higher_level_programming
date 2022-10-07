-- create database 'hbtn_0d_usa' if it doens't exist
-- create the table 'states' within it if it doesn't exist
-- states should have 'id' an int, auto-generated and unique and as primary key
-- also should have 'name' VARCHAR(256) and can't be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states 
(id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
