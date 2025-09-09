system cls

CREATE DATABASE FirstDB;

USE FirstDB;

-- Show all databases
SHOW DATABASES;

-- Use a specific database
USE database_name;

-- Show all tables in the current database
SHOW TABLES;

-- Show the structure of a specific table
DESCRIBE table_name;

-- Create a new database
CREATE DATABASE new_database_name;

-- Delete a database
DROP DATABASE database_name;

-- Create a new table
CREATE TABLE new_table_name (
    column1 datatype,
    column2 datatype,
    ...
);

-- Delete a table
DROP TABLE table_name;

-- Select all data from a table
SELECT * FROM table_name;

-- Insert a new row into a table
INSERT INTO table_name (column1, column2) VALUES (value1, value2);

-- Update data in a table
UPDATE table_name SET column1 = value1 WHERE condition;

-- Delete data from a table
DELETE FROM table_name WHERE condition;

-- Select data from a table with a specific condition
SELECT * FROM table_name WHERE column1 = value1;

-- Order the result set of a query
SELECT * FROM table_name ORDER BY column1;

-- Group the result set of a query
SELECT column1, COUNT(*) FROM table_name GROUP BY column1;

-- Join data from two tables
SELECT * FROM table1 JOIN table2 ON table1.column1 = table2.column1;
