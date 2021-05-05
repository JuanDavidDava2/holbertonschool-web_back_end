-- Write a SQL script that creates a
-- table users following these requirements:
-- script can be executed on any database
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255)
);