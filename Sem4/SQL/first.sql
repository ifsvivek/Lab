CREATE DATABASE FirstDB;

USE FirstDB;

CREATE TABLE Employees (
    EMPNO INT,
    ENAME VARCHAR(255),
    JOB VARCHAR(255),
    Manager_NO INT,
    SAL INT,
    DOB DATE
);

INSERT INTO
    Employees
VALUES
    (1, 'John', 'Manager', 0, 1000, '1990-01-01');

INSERT INTO
    Employees
VALUES
    (2, 'Jane', 'Manager', 0, 1000, '1990-01-01');

INSERT INTO
    Employees
VALUES
    (3, 'Jack', 'Manager', 0, 1000, '1990-01-01');

INSERT INTO
    Employees
VALUES
    (4, 'Jill', 'Manager', 0, 1000, '1990-01-01');

INSERT INTO
    Employees
VALUES
    (5, 'James', 'Manager', 0, 1000, '1990-01-01');

INSERT INTO
    Employees
VALUES
    (6, 'Jenny', 'Manager', 0, 1000, '1990-01-01');

INSERT INTO
    Employees
VALUES
    (7, 'Jasper', 'Manager', 0, 1000, '1990-01-01');

INSERT INTO
    Employees
VALUES
    (8, 'Jasmine', 'Manager', 0, 1000, '1990-01-01');

INSERT INTO
    Employees
VALUES
    (9, 'Jared', 'Manager', 0, 1000, '1990-01-01');

INSERT INTO
    Employees
VALUES
    (10, 'Jade', 'Manager', 0, 1000, '1990-01-01');

INSERT INTO
    Employees
VALUES
    (11, 'Jared', 'Manager', 0, 1000, '1990-01-01');

INSERT INTO
    Employees
VALUES
    (12, 'Jade', 'Manager', 0, 1000, '1990-01-01');

SELECT
    *
FROM
    Employees;

system cls
DELETE FROM
    Employees
WHERE
    EMPNO = 3
    AND ENAME = 'Jack'
    AND JOB = 'Manager'
    AND Manager_NO = 0
    AND SAL = 1000
    AND DOB = '1990-01-01';

ALTER TABLE
    Employees
ADD
    PRIMARY KEY (EMPNO);