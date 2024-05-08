-- Create a table called Employee & execute the following.
-- Employee(EMPNO,ENAME,JOB, MANAGER_NO, SAL, COMMISSION)
-- 1. Create a user and grant all permissions to theuser.
-- 2. Insert the any three records in the employee table contains attributes
-- EMPNO,ENAME JOB, MANAGER_NO, SAL, COMMISSION and use rollback.
-- Check the result.
-- 3. Add primary key constraint and not null constraint to the employee table.
-- 4. Insert null values to the employee table and verify the result. 
-- 1. Create a user and grant all permissions to theuser.
-- Create a table called Employee
CREATE TABLE Employee (
    EMPNO INT PRIMARY KEY,
    ENAME VARCHAR(255) NOT NULL,
    JOB VARCHAR(255) NOT NULL,
    MANAGER_NO INT NOT NULL,
    SAL INT NOT NULL,
    COMMISSION INT
);

-- Create a user and grant all permissions to theuser.
CREATE USER 'theuser'@'localhost' IDENTIFIED BY 'theuser';
GRANT ALL PRIVILEGES ON *.* TO 'theuser'@'localhost';

-- Start a transaction
START TRANSACTION;

-- Insert three records into the employee table
INSERT INTO Employee VALUES (1, 'John', 'Manager', 1, 10000, 1000);
INSERT INTO Employee VALUES (2, 'Doe', 'Manager', 1, 10000, 1000);
INSERT INTO Employee VALUES (3, 'Jane', 'Manager', 1, 10000, 1000);

-- Rollback the transaction
ROLLBACK;

-- Insert null values into the employee table
INSERT INTO Employee VALUES (4, 'John', 'Manager', 1, 10000, NULL);
INSERT INTO Employee VALUES (5, 'Doe', 'Manager', 1, 10000, NULL);
INSERT INTO Employee VALUES (6, 'Jane', 'Manager', 1, 10000, NULL);

-- Select all records from the employee table
SELECT * FROM Employee;

-- Drop the table Employee
DROP TABLE Employee;

-- Drop the user theuser
DROP USER 'theuser'@'localhost';

-- Exit from the SQL prompt
EXIT;