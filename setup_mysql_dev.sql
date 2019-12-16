-- Prepares a "hbnb_dev_db" database with a "hbnb_dev" user at localhost
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`
	CHARSET utf8mb4
	COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
