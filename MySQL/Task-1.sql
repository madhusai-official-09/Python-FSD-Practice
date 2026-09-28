-- TASK-1
-- 1.Write a query to display the employee name, salary, and salary after adding ₹5,000. 
-- Write a query to display employees whose salary is between 25,000 and 40,000.

use company_details;
select * from employee;

select ename,sal,sal+5000 as sal_add_5k from employee;
select ename from employee where sal >= 2500 and sal<=4000;

-- 2.Write a SQL query to display each employee’s name, salary, and salary after deducting 5% as tax using arithmetic operators. 
-- Write a SQL query to display each employee’s name, salary, and annual salary after a 10% increment, using arithmetic operators.

select ename,sal,sal-(sal*5/100) as ded_5 from employee;
select ename,sal,annual_sal+(annual_sal*10/100) as inc_10 from employee;