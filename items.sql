CREATE TABLE items (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    1code VARCHAR(50) NOT NULL,
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
    ('10001', 'Product 1',  'First product',                0),
    ('10002', 'Product 2',  'Second product',               1),
    ('10003', 'Product 3',  NULL,                            0),
    ('10004', 'Product 4',  'Fourth product',               1),
    ('10005', 'Product 5',  'Fifth product',                0),
    ('10006', 'Product 6',  NULL,                            1),
    ('10007', 'Product 7',  'Seventh product',              0),
    ('10008', 'Product 8',  'Eighth product',               1),
    ('10009', 'Product 9',  NULL,                            0),
    ('10010', 'Product 10', 'Tenth product',                1),
    ('10011', 'Product 11', 'Eleventh product',             0),
    ('10012', 'Product 12', NULL,                            1),
    ('10013', 'Product 13', 'Thirteenth product',           0),
    ('10014', 'Product 14', 'Fourteenth product',           1),
    ('10015', 'Product 15', NULL,                            0),
    ('10016', 'Product 16', 'Sixteenth product',            1),
    ('10017', 'Product 17', 'Seventeenth product',          0),
    ('10018', 'Product 18', 'Eighteenth product',           1),
    ('10019', 'Product 19', NULL,                            0),
    ('10020', 'Product 20', 'Twentieth product',            1),
    ('10021', 'Product 21', 'Twenty‑first product',         0),
    ('10022', 'Product 22', 'Twenty‑second product',        1),
    ('10023', 'Product 23', NULL,                            0),
    ('10024', 'Product 24', 'Twenty‑fourth product',        1),
    ('10025', 'Product 25', 'Twenty‑fifth product',         0),
    ('10026', 'Product 26', 'Twenty‑sixth product',         1),
    ('10027', 'Product 27', NULL,                            0),
    ('10028', 'Product 28', 'Twenty‑eighth product',        1),
    ('10029', 'Product 29', 'Twenty‑ninth product',         0),
    ('10030', 'Product 30', 'Thirtieth product',            1),
    ('10031', 'Product 31', 'Thirty‑first product',         0),
    ('10032', 'Product 32', 'Thirty‑second product',        1),
    ('10033', 'Product 33', NULL,                            0),
    ('10034', 'Product 34', 'Thirty‑fourth product',        1),
    ('10035', 'Product 35', 'Thirty‑fifth product',         0),
    ('10036', 'Product 36', 'Thirty‑sixth product',         1),
    ('10037', 'Product 37', NULL,                            0),
    ('10038', 'Product 38', 'Thirty‑eighth product',        1),
    ('10039', 'Product 39', 'Thirty‑ninth product',         0),
    ('10040', 'Product 40', 'Fortieth product',             1),
    ('10041', 'Product 41', 'Forty‑first product',          0),
    ('10042', 'Product 42', 'Forty‑second product',         1),
    ('10043', 'Product 43', NULL,                            0),
    ('10044', 'Product 44', 'Forty‑fourth product',         1),
    ('10045', 'Product 45', 'Forty‑fifth product',          0),
    ('10046', 'Product 46', 'Forty‑sixth product',          1),
    ('10047', 'Product 47', NULL,                            0),
    ('10048', 'Product 48', 'Forty‑eighth product',         1),
    ('10049', 'Product 49', 'Forty‑ninth product',          0),
    ('10050', 'Product 50', 'Fiftyth product',              1);






    TRUNCATE items