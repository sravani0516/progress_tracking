USE company;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10,2),
    hire_date DATE
);

INSERT INTO employees VALUES
(1, 'Ravi', 50000, '2022-01-01'),
(2, 'Priya', 70000, '2021-05-10'),
(3, 'Arjun', 40000, '2023-03-15');

SELECT name,
CASE
    WHEN salary > 60000 THEN 'High'
    ELSE 'Normal'
END AS salary_level
FROM employees;
