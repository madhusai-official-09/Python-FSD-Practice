create database company_details;
use company_details;
create table employee(empno int,ename varchar(50), job varchar(50), hiredate date, mgr int, sal int, comm int, deptno int);
alter table employee add constraint n_empno primary key(empno);
desc employee;
insert into employee values (7370,'SMITH','CLERK','1980-12-17',7902,800, null,20);
update employee set job = 'CLERK' where empno = 7369;
delete from employee where empno = 7369;
select * from employee;
INSERT INTO employee VALUES
(7499, 'ALLEN', 'SALESMAN', '1981-02-20', 7698, 1600, 300, 30),
(7521, 'WARD', 'SALESMAN', '1981-02-22', 7698, 1250, 500, 30),
(7566, 'JONES', 'MANAGER', '1981-04-02', 7839, 2975, NULL, 20),
(7654, 'MARTIN', 'SALESMAN', '1981-09-28', 7698, 1250, 1400, 30),
(7698, 'BLAKE', 'MANAGER', '1981-05-01', 7839, 2850, NULL, 30),
(7782, 'CLARK', 'MANAGER', '1981-06-09', 7839, 2450, NULL, 10),
(7788, 'SCOTT', 'ANALYST', '1987-04-19', 7566, 3000, NULL, 20),
(7839, 'KING', 'PRESIDENT', '1981-11-17', NULL, 5000, NULL, 10),
(7844, 'TURNER', 'SALESMAN', '1981-09-08', 7698, 1500, 0, 30),
(7876, 'ADAMS', 'CLERK', '1987-05-23', 7788, 1100, NULL, 20),
(7900, 'JAMES', 'CLERK', '1981-12-03', 7698, 950, NULL, 30),
(7902, 'FORD', 'ANALYST', '1981-12-03', 7566, 3000, NULL, 20),
(7934, 'MILLER', 'CLERK', '1982-01-23', 7782, 1300, NULL, 10);

-- 7.WRITE A QUERY TO DISPLAY ALL THE EMPLOYEE DETAILS FROM THE EMPLOYEE TABLE?
select * from employee;

-- 8.WRITE A QUERY TO DISPLAY ALL THE EMPLOYEE NAMES AND SALARY DETAILS FROM THE EMPLOYEE TABLE?
select ename,sal from employee ;

-- 9.WRITE A QUERY TO DISPLAY ONLY EMPLOYEE NAMES AND HIREDATE FROM THE EMPLOYEE TABLE?
select ename,hiredate from employee;

-- 10.WAQTD NAMES OF ALL THE EMPLOYEES
select ename  from employee;

-- 11.WAQTD NAME AND SALARY GIVEN TO ALL THE EMPLOYEES
select ename,sal from employee;

-- 12.WAQTD NAME AND COMMISSION GIVEN TO ALL THE EMPLOYEES.
select ename,comm from employee;

-- 13.WAQTD EMPLOYEE ID AND DEPARTMENT NUMBER OF ALL THE EMPLOYEES IN EMP TABLE.
select empno,deptno from employee;

-- 14.WAQTD ENAME AND HIREDATE OF ALL THE EMPLOYEES.
select ename, hiredate from employee;

-- 15.WAQTD NAME AND DESIGNATION OF ALL THE EMPLPOYEES.
select ename,job from employee;

-- 16.WAQTD NAME, JOB AND SALARY GIVEN ALL THE EMPLOYEES.
select ename,job,sal from employee;

-- 19.WAQTD NAME AND ANNUAL SALARY OF THE EMPLOYEES
select *,(sal*12) as annual_sal from employee;
insert into employee(annual_sal)values (sal*12);
update employee set annual_sal = sal*12;
set sql_safe_updates = 0;
alter table employee add gmail varchar(150);
update employee set gmail = concat(ename , "@gmail.com");


-- 20.WAQTD ALL THE DETAILS OF THE EMPLOYEE ALONG WITH ANNUAL SALARY
select * from employee;
SELECT count(distinct job ) from employee;
commit;

-- 21.WAQTD NAME AND SALARY OF AN EMPLOYEE WITH A DEDUCTION OF 10% .
select ename,sal,sal-(sal*10/100) as deduction from employee;

-- 22.WAQTD ENAME AND JOB FOR ALL THE EMPLOYEE WITH THEIR HALF TERM SALARY.
select ename,sal,(annual_sal/2) as half_term_sal from employee;

-- 23.WAQTD ALL THE DETAILS OF THE EMPLOYEES ALONG WITH AN ANNUALBONUS OF 2000.
select *,(annual_sal+2000) as annual_bonus from employee;

-- 24.WAQTD NAME SALARY AND SALARY WITH A HIKE OF 10%.
select ename,sal,sal+(sal*10/100) as hike_sal from employee;

-- 25.WAQTD NAME AND SALARY WITH DEDUCTION OF 25%.
select ename,sal,sal-(sal*25/100) as deduction from employee;

-- 26.WAQTD NAME AND SALARY WITH MONTHLY HIKE OF 50.
select ename,sal,sal+50 as hike_sal from employee;

-- 27.WAQTD NAME AND ANNUAL SALARY WITH DEDUCTION OF 10%.
select ename,sal,annual_sal - (annual_sal*10/100) as ded_sal from employee;

--  28.WAQTD TOTAL SALARY GIVEN TO EACH EMPLOYEE (SAL+COMM).
select sal+comm as total_sal from employee;

-- 29.WAQTD DETAILS OF ALL THE EMPLOYEES ALONG WITH ANNUAL SALARY.
select * from employee;

-- 30.WAQTD NAME AND DESIGNATION ALONG WITH 100 PENALTY IN SALARY.
select ename,job,sal-100 as penalty from employee;

-- Where Clause

-- 31.WAQTD THE ANNUAL SALARY OF THE EMPLOYEE WHOS NAME IS ALLEN.
select ename,annual_sal from employee where ename = "ALLEN";

-- 32.WAQTD NAME OF THE EMPLOYEES WORKING AS CLERK.
select ename,job from employee where job = "CLERK";

-- 33.WAQTD SALARY OF THE EMPLOYEES WHO ARE WORKING AS SALESMAN.
select sal from employee where job = "SALESMAN";

-- 34.WAQTD DETAILS OF THE EMP WHO EARNS MORE THAN 2000.
select * from employee where sal>2000;

-- 35.WAQTD DETAILS OF THE EMP WHOS NAME IS JONES.
select * from employee where ename = "JONES";

-- 36.WAQTD DETAILS OF THE EMP WHO WAS HIRED AFTER 01-JAN-81.
select * from employee where year(hiredate)>1981;

-- 37.WAQTD NAME AND SAL ALONG WITH HIS ANNUAL SALARY IF THE ANNUAL SALARY IS MORE THAN 12000.
select ename,sal from employee where annual_sal>12000;

-- 38.WAQTD EMPNO OF THE EMPLOYEES WHO ARE WORKING IN DEPT 30.
select empno from employee where deptno = 30;

-- 39.WAQTD ENAME AND HIREDATE IF THEY ARE HIRED BEFORE 1981.
select ename,hiredate from employee where year(hiredate)<1981;

-- 40.WAQTD DETAILS OF THE EMPLOYEES WORKING AS MANAGER.
select * from employee where job = "MANAGER";

-- 41.WAQTD NAME AND SALARY GIVEN TO AN EMPLOYEE IF EMPLOYEE EARNS A COMMISSION OF RUPEES 1400.
select ename,sal from employee where comm = 1400;

-- 42.WAQTD DETAILS OF EMPLOYEES HAVING COMMISSION MORE THAN SALARY.
select * from employee where comm>sal;

-- 43.WAQTD EMPNO OF EMPLOYEES HIRED BEFORE THE YEAR 1987.
select empno from employee where year(hiredate)<1987;

-- 44.WAQTD DETAILS OF EMPLOYEES WORKING AS AN N ANALYST.
select * from employee where job = 'ANALYST';

-- 45.WAQTD DETAILS OF EMPS EARNING MORE THAN 2000 RUPEES PER MONTH.
select * from employee where sal > 2000;