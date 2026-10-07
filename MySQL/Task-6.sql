use employee_db;
select * from employee;

-- 1.Write a query to find the top 3 highest-paid employees. 
with temp as(
select full_name ,salary, dense_rank() over(order by salary desc) as d_r from employee 
) select * from temp where d_r between 1 and 3;

-- 2.Write a query to assign a row number to each employee based on salary from highest to lowest. 
with temp as(
select full_name ,salary, row_number() over(order by salary desc) as row_num from employee 
) select * from temp;

-- 3.Write a query to display each employee's salary and the difference between their salary and the highest salary.
select full_name,salary, max(salary) over() - salary as 'sal_diff' from employee;

-- 4.Write a query to find the second-highest salary.
with temp as(
select full_name ,salary, dense_rank() over(order by salary desc) as d_r from employee 
) select * from temp where d_r = 2;

-- 5.Write a query to display each employee along with the average salary of their department. 
select full_name,avg(salary) over(partition by dept_id) from employee;

-- 6.Write a query to display each employee's salary along with the previous employee's salary when employees are ordered by salary.
select full_name,salary, LAG(salary) over(order by salary) as previous_salary
from employee;

-- 7.Write a query to display each employee's salary along with the next employee's salary.
select full_name,salary, LEAD(salary) over(order by salary) as NEXT_salary
from employee;