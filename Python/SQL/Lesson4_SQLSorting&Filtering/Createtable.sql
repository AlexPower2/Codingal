CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    status VARCHAR(20) -- Example: 'Fraud' or 'Legit'
);INSERT INTO employees (employee_id, name, department, salary, status) 
VALUES 
(1, 'Alice Johnson', 'Finance', 75000, 'Legit'),
(2, 'Bob Smith', 'HR', 65000, 'Fraud'),
(3, 'Charlie Brown', 'IT', 80000, 'Legit'),
(4, 'David White', 'Finance', 72000, 'Fraud');SELECT * FROM employees WHERE status = 'Fraud';