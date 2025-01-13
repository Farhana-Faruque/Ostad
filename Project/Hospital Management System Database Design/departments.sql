CREATE TABLE department(
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100),
    dept_location VARCHAR(100)
);

INSERT INTO department(dept_name, dept_location) VALUES
('Cardiology', 'Building A'),
('Neurology', 'Building B'),
('Orthopedics', 'Building C'),
('Pediatrics', 'Building D'),
('General Medicine', 'Building E');