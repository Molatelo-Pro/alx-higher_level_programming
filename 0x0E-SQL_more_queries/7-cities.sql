-- create_database_and_table.sql

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create the states table if it doesn't exist (required for the foreign key reference)
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Create the cities table
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    UNIQUE (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
