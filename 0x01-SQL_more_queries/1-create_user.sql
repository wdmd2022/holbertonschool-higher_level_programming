-- now let's create a user (if they don't already exist) on our server,
-- with all privileges, if he doesn't exist, with name user_0d_1 and pass user_0d_1_pwd
CREATE USER IF NOT EXISTS `user_0d_1`@`localhost` IDENTIFIED BY `user_0d_1_pwd`;
GRANT ALL PRIVILEGES ON *.* TO `user_0d_1`@`localhost` WITH GRANT OPTION;
FLUSH PRIVILEGES;
