create table department(deptno int,dname varchar(50), loc varchar(50));
select * from department;
insert into department values(10,'accounting','new york'),(20,'research','dallas'),(30,'sales','chicago'),(40,'operations','boston');
-- 17.WAQTD DNAMES PRESENT IN DEPARTMENT TABLE.
select dname from department;

-- 18.WAQTD DNAME AND LOCATION PRESENT IN DEPT TABLE.
select dname,loc from department;
