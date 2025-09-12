CREATE DATABASE tinstore;
USE tinstore;
CREATE TABLE items (
    barcode INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    date_added DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    notes TEXT NULL,
    value INT NULL,
    sold BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (barcode)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- testing
INSERT INTO items (barcode, name, date_added, notes, value, sold) VALUES
(1001, 'Laptop', '2025-08-15 10:00:00', 'High-end gaming laptop.', 1500, FALSE),
(1002, 'Smartphone', '2025-08-16 11:30:00', 'Latest model with a cracked screen.', 700, FALSE),
(1003, 'Headphones', '2025-08-17 14:45:00', 'Noise-cancelling over-ear headphones.', 250, FALSE),
(1004, 'Desk Chair', '2025-08-18 09:15:00', 'Ergonomic office chair.', 300, FALSE),
(1005, 'Monitor', '2025-08-19 16:20:00', '4K ultra-wide monitor.', 550, FALSE),
(1006, 'Keyboard', '2025-08-20 12:00:00', 'Mechanical keyboard with RGB lighting.', 120, FALSE),
(1007, 'Mouse', '2025-08-21 08:30:00', 'Wireless gaming mouse.', 80, FALSE),
(1008, 'Webcam', '2025-08-22 13:10:00', 'Full HD webcam.', 60, FALSE),
(1009, 'Speakers', '2025-08-23 17:00:00', 'Bluetooth bookshelf speakers.', 200, FALSE),
(1010, 'External Hard Drive', '2025-08-24 10:50:00', '1TB portable hard drive.', 75, FALSE);


    TRUNCATE items

    CREATE TABLE users (
    username VARCHAR(50) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    PRIMARY KEY (username)