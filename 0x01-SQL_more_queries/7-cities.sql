-- create database 'hbtn_0d_usa' if it doens't exist
-- create the table 'states' within it if it doesn't exist
-- states should have 'id' an int, auto-generated and unique and as primary key
-- also should have 'name' VARCHAR(256) and can't be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities 
(id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT, 
state_id INT NOT NULL FOREIGN KEY REFERENCES hbtn_0d_usa.states(id),
name VARCHAR(256) NOT NULL);
