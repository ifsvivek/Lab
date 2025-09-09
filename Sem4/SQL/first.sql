-- Create a table called Employee & execute the following.
-- Employee(EMPNO,ENAME,JOB, MANAGER_NO, SAL, COMMISSION)
-- 1. Create a user and grant all permissions to theuser.
-- 2. Insert the any three records in the employee table contains attributes
-- EMPNO,ENAME JOB, MANAGER_NO, SAL, COMMISSION and use rollback.
-- Check the result.
-- 3. Add primary key constraint and not null constraint to the employee table.
-- 4. Insert null values to the employee table and verify the result. 


CREATE DATABASE FirstDB;

USE FirstDB;

CREATE TABLE Employee(
    EMPNO INT,
    ENAME VARCHAR(50),
    JOB VARCHAR(50),
    MANAGER_NO INT,
    SAL INT,
    COMMISSION INT
);

CREATE USER 'FirstUser'@'localhost';

GRANT ALL PRIVILEGES ON FirstDB.Employee TO 'FirstUser'@'localhost';

START TRANSACTION;

INSERT INTO Employee(EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION) VALUES(1, 'John', 'Manager', 0, 10000, 1000);

INSERT INTO Employee(EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION) VALUES(2, 'Jane', 'Manager', 0, 10000, 1000);

INSERT INTO Employee(EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION) VALUES(3, 'Jack', 'Manager', 0, 10000, 1000);

SELECT * FROM Employee;

ROLLBACK;

SELECT * FROM Employee;

ALTER TABLE Employee ADD PRIMARY KEY(EMPNO);

ALTER TABLE Employee MODIFY EMPNO INT NOT NULL;

INSERT INTO Employee(EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION) VALUES(NULL, 'John', 'Manager', 0, 10000, 1000);

INSERT INTO Employee(EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION) VALUES(4, 'Jane', 'Manager', 0, 10000, 1000);

INSERT INTO Employee(EMPNO, ENAME, JOB, MANAGER_NO, SAL, COMMISSION) VALUES(5, 'Jack', 'Manager', 0, 10000, 1000);

SELECT * FROM Employee;

DROP TABLE Employee;

DROP USER 'FirstUser'@'localhost';