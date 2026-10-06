use employee_db;
select * from employee;

-- 1.Display the annual salary of the employee whose name is Sai.
select full_name,salary,ANNUAL_SALARY from employee where full_name = 'Sai';

-- 2.Show the names of employees working as Backend Developer.
select * from employee where role = 'Backend Developer';

-- 3.Find the salary of employees who are working as QA Engineer.
select full_name,salary,annual_salary,role from employee where role = 'QA Engineer';

-- 4.Get the details of employees who earn more than ₹2000 as bonus.
select * from employee where bonus>2000;

-- 5.Display all the details of the employee whose name is Ravi.
select * from employee where full_name = 'Ravi';

-- 6.Find the details of employees who joined after '2021-01-01'.
select * from employee where year(join_date)>2021;

-- 7.Show the name and salary along with annual salary of employees earning more than ₹120000 per year.
select full_name,salary,annual_salary from employee where annual_salary>120000;

-- 8.Display the EMP_ID of employees who are working in department 3.
select emp_id,full_name,dept_id from employee where dept_id = 3;

-- 9.Show name and join date of employees who joined before '2020-01-01'.
select full_name,join_date from employee where year(join_date)<2020;

-- 10.Find the details of employees working as Technical Lead.
select * from employee where role = 'Technical Lead';