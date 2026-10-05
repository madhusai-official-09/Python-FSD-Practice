CREATE DATABASE employee_db;

USE employee_db;

CREATE TABLE employee (
    EMP_ID INT PRIMARY KEY,
    FULL_NAME VARCHAR(50),
    ROLE VARCHAR(50),
    JOIN_DATE DATE,
    REPORTS_TO INT NULL,
    SALARY DECIMAL(10,2),
    BONUS DECIMAL(10,2) NULL,
    DEPT_ID INT,
    BLOOD_GROUP VARCHAR(5),
    EMP_TYPE VARCHAR(20),
    GENDER VARCHAR(10),
    DOB DATE
);

-- Insert Employee Data
INSERT INTO employee
(EMP_ID, FULL_NAME, ROLE, JOIN_DATE, REPORTS_TO, SALARY, BONUS, DEPT_ID, BLOOD_GROUP, EMP_TYPE, GENDER, DOB)
VALUES
(1127, 'Vani', 'Frontend Developer', '2021-03-10', 1739, 80000, 5000, 1, 'A+', 'Full-time', 'Female', '1993-07-19'),

(1182, 'Sai Kiran', 'QA Engineer', '2020-05-12', 1739, 70000, NULL, 2, 'B+', 'Intern', 'Male', '1992-01-12'),

(1261, 'Ravi', 'DevOps Engineer', '2021-11-25', 1846, 90000, 7000, 3, 'AB-', 'Full-time', 'Male', '1995-09-08'),

(1053, 'Mani', 'Backend Developer', '2022-06-15', 1053, 85000, 6000, 1, 'O+', 'Contract', 'Male', '1999-03-21'),

(1344, 'Sai', 'Cybersecurity Analyst', '2023-02-01', 1846, 95000, NULL, 4, 'O-', 'Full-time', 'Male', '1991-10-05'),

(1432, 'Harika', 'UI/UX Designer', '2020-10-18', 1739, 78000, 4000, 1, 'A-', 'Intern', 'Female', '1996-04-30'),

(1580, 'Krishna Reddy', 'System Administrator', '2019-09-01', 1846, 87000, 5500, 3, 'B-', 'Full-time', 'Male', '1989-01-19'),

(1615, 'Soumya', 'Database Engineer', '2021-12-05', 1739, 91000, NULL, 1, 'O+', 'Full-time', 'Female', '1993-06-27'),

(1739, 'Sirisha', 'Technical Lead', '2018-05-14', NULL, 130000, 12000, 1, 'AB+', 'Full-time', 'Female', '1985-07-11'),

(1846, 'Tejaswini', 'Cloud Architect', '2017-08-20', NULL, 140000, 15000, 3, 'A+', 'Full-time', 'Female', '1987-02-03'),

(1957, 'Vishnu Priya', 'HR Executive', '2022-07-01', 1068, 65000, NULL, 5, 'B+', 'Contract', 'Female', '1995-11-14'),

(1068, 'Sireesha', 'HR Manager', '2020-10-15', NULL, 95000, 6000, 5, 'A-', 'Full-time', 'Female', '1990-08-06'),

(1133, 'Raju', 'Network Security Engineer', '2021-04-12', 1053, 88000, 7000, 4, 'O+', 'Full-time', 'Male', '1993-01-09'),

(1209, 'Charan', 'Business Analyst', '2020-10-01', 1739, 78000, NULL, 1, 'B+', 'Intern', 'Male', '1992-08-23'),

(1375, 'Tarun Kumar', 'Automation Tester', '2023-01-19', 1182, 73000, 4000, 2, 'O-', 'Full-time', 'Male', '1994-12-12'),

(1482, 'Lakshmi', 'Recruiter', '2022-09-03', 1068, 60000, 2000, 5, 'A+', 'Full-time', 'Female', '1996-03-29'),

(1571, 'Srikanth', 'DevOps Specialist', '2021-02-25', 1846, 92000, 6000, 3, 'B-', 'Full-time', 'Male', '1990-10-04'),

(1677, 'Pranavi', 'Penetration Tester', '2023-05-10', 1344, 96000, NULL, 4, 'AB+', 'Full-time', 'Female', '1995-01-17'),

(1763, 'Pavan', 'Software Architect', '2019-07-30', 1127, 145000, 20000, 1, 'O+', 'Contract', 'Male', '1988-05-25'),

(1894, 'Jahnavi', 'HR Coordinator', '2020-11-05', 1068, 63000, 2500, 5, 'B-', 'Full-time', 'Female', '1993-09-22');

select * From employee;


-- 1. Find employees whose SALARY is greater than BONUS and whose EMP_TYPE is 'Contract'.
select * from employee where salary>bonus and emp_type = 'Contract';

-- 2. Show employees whose salary is more than 85000 and BONUS is not NULL.
select * from employee where salary>85000 and BONUS is not NULL;

-- 3. Display employees whose SALARY is not between 60000 and 90000.
select * from employee where salary not between 60000 and 90000;

-- 6. Find employees whose ROLE is either 'Backend Developer' or 'Frontend Developer', and whose DEPT_ID is 1 or 2.
select * from employee where (role = 'Backend Developer' or role = 'Frontend Developer') and (dept_id = 1 or dept_id = 2);

-- 7. Display employees whose REPORTS_TO is in (1739, 1846, 1068) but whose DEPT_ID is not 1.
select * from employee where reports_to in (1739, 1846, 1068) and dept_id != 1;

-- 11. List employees whose name does not contain 'a', whose ROLE contains 'Engineer', and whose SALARY is greater than 60000.
select * from employee where full_name not like "%a%" and role like  '%Engineer%' and salary > 60000;

-- 12. Find employees who are either in DEPT_ID 1 or 3, or whose ROLE is 'HR Manager', but exclude employees whose EMP_TYPE is 'Intern'.
select * from employee where (dept_id in (1,3) or role = 'HR Manager') and (emp_type != 'Intern');