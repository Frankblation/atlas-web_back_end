-- SQL script to create the users table with constraints

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Auto-incrementing primary key
    email VARCHAR(255) NOT NULL UNIQUE,  -- Email, unique and non-null
    name VARCHAR(255),                   -- Name, string with a max length of 255
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'  -- Country enum with default value 'US'
);
