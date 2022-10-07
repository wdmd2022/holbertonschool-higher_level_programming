-- create the database hbtn_0d_2 (unless it already exists)
-- create the user user_0d_2 (if they don't exist)
-- the user should have pass 'user_0d_2_pwd'
-- they should have SELECT privilege in the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* to 'user_0d_2'@'localhost';
