use employee_db;
select * from employee;
show columns from employee;
alter table employee add column EMAIL VARCHAR(50);
UPDATE employee
SET EMAIL = CONCAT(LOWER(REPLACE(TRIM(FULL_NAME), ' ', '.')),'@gmail.com')
WHERE EMP_ID > 0;

-- 1.Display each employee's name in the format LASTNAME, Firstname using string functions.

-- 2.Display employee names after removing all leading and trailing spaces, and convert the names to uppercase.
select trim(upper(full_name)) from employee;

-- 3.Display the first 3 characters and last 3 characters of each employee's name as a single value separated by -.
select concat(substring(full_name,1,3), '-', substring(full_name,-3)) as new_name from employee;

-- 4.Display each employee's email username separately from the domain name. Example: john@gmail.com → john | gmail.com
select concat(substring_index(email,'@',1), ' | ', substring_index(email,'@',-1)) as sep_email from employee;

-- 5.Display employee names with all occurrences of the letter a replaced by @, without changing the case of other characters.
select replace(full_name, 'a', '@') as name_replace from employee;

-- 6.Display the employee name and its reverse, but only for employees whose name contains more than 5 characters.
select full_name, reverse(full_name) from employee where length(full_name)>5;

-- 7.Display each employee's name after removing all spaces from it and then show the resulting string length.
select full_name, replace(full_name,' ',''), length(replace(full_name,' ','')) as len_name from employee;

-- 8.Display employee names in the format `First 2 characters + last 2 characters`, using string functions. Example: Alexander → Aler
select full_name,concat(substring(full_name,1,2),substring(full_name,-2)) as new_name from employee;

-- 9.Display the employee name and extract the text before the first space. Example: Rahul Kumar → Rahul
select full_name,substring_index(full_name,' ', 1) as new_name from employee;

-- 10. Display each employee's name with the first character converted to uppercase and the remaining characters converted to lowercase.
select full_name,concat(upper(substring(full_name,1,1)),lower(substring(full_name,2))) as new_name from employee;