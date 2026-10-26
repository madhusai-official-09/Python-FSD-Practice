CREATE DATABASE employee_task_tracker;
USE employee_task_tracker;

CREATE TABLE employees (
id INT auto_increment primary key,
name varchar(100) not null,
role varchar(50),
email varchar(100) unique,
created_at timestamp default current_timestamp);

describe employees;

INSERT INTO employees (name, role, email) VALUES ('Ravi Kumar', 'Developer', 'ravi@gmail.com');
UPDATE employees set role = 'Senior Developer' where id = 1;

select * from employees;

DELETE FROM employees where id = 1;

create table tasks(
id int auto_increment primary key,
title varchar(100),
description varchar(200),
status varchar(50),
due_date date
);

describe tasks;

alter table tasks modify status varchar(50) DEFAULT 'Pending';

create table assigned_tasks(
id int auto_increment primary key,
task_id int ,
employee_id int,
assigned_at timestamp default current_timestamp
);

describe assigned_tasks;

ALTER TABLE assigned_tasks
ADD constraint fk_assigned_employee
foreign key (employee_id)
references employees(id);

alter table assigned_tasks
add constraint fk_assigned_task
foreign key (task_id) 
references tasks(id);

select * from employees;
select * from tasks;

insert into employees (name, role, email) values ('Ravi Kumar', 'Developer', 'ravi@gmail.com');

INSERT INTO tasks (title, description, due_date)
VALUES (
    'Build Login Page',
    'Create login page for the application',
    '2026-10-30'
);

select id, name from employees;
select id, title from tasks;

insert into assigned_tasks(task_id,employee_id)
values (
1,
3
);

select * from assigned_tasks;

select employees.name,
employees.role,
tasks.title,
assigned_tasks.assigned_at
from assigned_tasks
join employees on assigned_tasks.employee_id = employees.id
join tasks on assigned_tasks.task_id = tasks.id
where tasks.status = 'Pending';

SELECT title, status, due_date
FROM tasks
ORDER BY due_date ASC;

CREATE TABLE comments (
id int auto_increment primary key,
task_id int ,
employee_id int,
comment_text varchar(255),
created_at datetime default current_timestamp
);

describe comments;

alter table comments
add constraint fk_comments_task
foreign key (task_id)
references tasks(id);

alter table comments
add constraint fk_comments_employee
foreign key (employee_id)
references employees(id);

show tables;
