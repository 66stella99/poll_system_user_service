DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    address VARCHAR(300) NOT NULL,
    joining_date DATE NOT NULL,
    is_registered BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (id),
    UNIQUE KEY uq_users_email (email)
);


INSERT INTO users (first_name, last_name, email, age, address, joining_date, is_registered) VALUES
    ('Alice', 'Smith', 'alice@example.com', 28, '12 Herzl St, Tel Aviv', '2023-01-15', TRUE),
    ('Bob', 'Johnson', 'bob@example.com', 35, '5 Jaffa Rd, Jerusalem', '2023-03-22', TRUE),
    ('Charlie', 'Brown', 'charlie@example.com', 42, '8 HaNassi Blvd, Haifa', '2023-06-01', TRUE),
    ('Dana', 'White', 'dana@example.com', 23, '3 Rothschild Blvd, Tel Aviv', '2024-02-10', FALSE),
    ('Eve', 'Black', 'eve@example.com', 31, '20 Weizmann St, Rehovot', '2024-07-30', FALSE);
