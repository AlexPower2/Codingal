CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10,2)
);INSERT INTO employees (employee_id, name, department, salary) VALUES 
(1, 'Alice', 'HR', 50000),
(2, 'Bob', 'IT', 75000),
(3, 'Charlie', 'Finance', 60000),
(4, 'David', 'IT', 80000),
(5, 'Emma', 'HR', 55000);SELECT SUM(salary) AS total_salary FROM employees;SELECT AVG(salary) AS average_salary FROM employees;SELECT COUNT(DISTINCT department) AS total_departments FROM employees;