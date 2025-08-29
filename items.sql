CREATE TABLE items (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    barcode VARCHAR(50) NOT NULL,
    name VARCHAR(255) NOT NULL,
    date_added DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    notes TEXT NULL,
    value INT NOT_NULL,
    sold BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- testing

INSERT INTO items (barcode, name, notes, sold)
VALUES
    ('BAR0001', 'Product 1',  'First product',                0),
    ('BAR0002', 'Product 2',  'Second product',               1),
    ('BAR0003', 'Product 3',  NULL,                            0),
    ('BAR0004', 'Product 4',  'Fourth product',               1),
    ('BAR0005', 'Product 5',  'Fifth product',                0),
    ('BAR0006', 'Product 6',  NULL,                            1),
    ('BAR0007', 'Product 7',  'Seventh product',              0),
    ('BAR0008', 'Product 8',  'Eighth product',               1),
    ('BAR0009', 'Product 9',  NULL,                            0),
    ('BAR0010', 'Product 10', 'Tenth product',                1),
    ('BAR0011', 'Product 11', 'Eleventh product',             0),
    ('BAR0012', 'Product 12', NULL,                            1),
    ('BAR0013', 'Product 13', 'Thirteenth product',           0),
    ('BAR0014', 'Product 14', 'Fourteenth product',           1),
    ('BAR0015', 'Product 15', NULL,                            0),
    ('BAR0016', 'Product 16', 'Sixteenth product',            1),
    ('BAR0017', 'Product 17', 'Seventeenth product',          0),
    ('BAR0018', 'Product 18', 'Eighteenth product',           1),
    ('BAR0019', 'Product 19', NULL,                            0),
    ('BAR0020', 'Product 20', 'Twentieth product',            1),
    ('BAR0021', 'Product 21', 'Twenty‑first product',         0),
    ('BAR0022', 'Product 22', 'Twenty‑second product',        1),
    ('BAR0023', 'Product 23', NULL,                            0),
    ('BAR0024', 'Product 24', 'Twenty‑fourth product',        1),
    ('BAR0025', 'Product 25', 'Twenty‑fifth product',         0),
    ('BAR0026', 'Product 26', 'Twenty‑sixth product',         1),
    ('BAR0027', 'Product 27', NULL,                            0),
    ('BAR0028', 'Product 28', 'Twenty‑eighth product',        1),
    ('BAR0029', 'Product 29', 'Twenty‑ninth product',         0),
    ('BAR0030', 'Product 30', 'Thirtieth product',            1),
    ('BAR0031', 'Product 31', 'Thirty‑first product',         0),
    ('BAR0032', 'Product 32', 'Thirty‑second product',        1),
    ('BAR0033', 'Product 33', NULL,                            0),
    ('BAR0034', 'Product 34', 'Thirty‑fourth product',        1),
    ('BAR0035', 'Product 35', 'Thirty‑fifth product',         0),
    ('BAR0036', 'Product 36', 'Thirty‑sixth product',         1),
    ('BAR0037', 'Product 37', NULL,                            0),
    ('BAR0038', 'Product 38', 'Thirty‑eighth product',        1),
    ('BAR0039', 'Product 39', 'Thirty‑ninth product',         0),
    ('BAR0040', 'Product 40', 'Fortieth product',             1),
    ('BAR0041', 'Product 41', 'Forty‑first product',          0),
    ('BAR0042', 'Product 42', 'Forty‑second product',         1),
    ('BAR0043', 'Product 43', NULL,                            0),
    ('BAR0044', 'Product 44', 'Forty‑fourth product',         1),
    ('BAR0045', 'Product 45', 'Forty‑fifth product',          0),
    ('BAR0046', 'Product 46', 'Forty‑sixth product',          1),
    ('BAR0047', 'Product 47', NULL,                            0),
    ('BAR0048', 'Product 48', 'Forty‑eighth product',         1),
    ('BAR0049', 'Product 49', 'Forty‑ninth product',          0),
    ('BAR0050', 'Product 50', 'Fiftyth product',              1);






    TRUNCATE items