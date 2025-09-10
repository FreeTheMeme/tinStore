CREATE DATABASE [IF NOT EXISTS] tinstore;
CREATE TABLE items (
    barcode INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    date_added DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    notes TEXT NULL,
    value INT NULL,
    sold BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (barcode)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE users (
    username VARCHAR(50) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    PRIMARY KEY (username
-- testing



    TRUNCATE items