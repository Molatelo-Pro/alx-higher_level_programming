-- list_cities_of_california.sql

-- Use the specified database
USE hbtn_0d_usa;

-- List all cities of California
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
