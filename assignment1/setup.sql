-- noinspection SqlNoDataSourceInspectionForFile

-- noinspection SqlDialectInspectionForFile

-- -----------------------------------------------------
-- Schema twitterdb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS twitterdb;

-- -----------------------------------------------------
-- Schema twitterdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS twitterdb DEFAULT CHARACTER SET utf8 ;
USE twitterdb;

-- -----------------------------------------------------
-- Table `followers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS followers ;

CREATE TABLE IF NOT EXISTS followers (
  user_id INT,
  follows_id INT
);

-- -----------------------------------------------------
-- Table `tweets`
-- -----------------------------------------------------
DROP TABLE IF EXISTS tweets ;

CREATE TABLE IF NOT EXISTS tweets (
  tweet_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT,
  tweet_ts DATETIME NOT NULL,
  tweet_text VARCHAR(140) NOT NULL
);
