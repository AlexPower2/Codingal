CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50),
    grade INT
);INSERT INTO customers (customer_id, name, city, grade) VALUES 
(1, 'John Doe', 'New York', 110),
(2, 'Jane Smith', 'Los Angeles', 90),
(3, 'Emily Davis', 'New York', 95),
(4, 'Michael Brown', 'Chicago', 120),
(5, 'David Wilson', 'New York', 105);SELECT * FROM customers WHERE city = 'New York' OR grade > 100;SELECT * FROM customers WHERE city = 'New York' AND grade > 100;