CREATE TABLE doctors(
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    doctor_name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    dept_id INT,
    FOREIGN KEY doctors(dept_id) REFERENCES department(department_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

INSERT INTO doctors (doctor_name, specialization, phone, dept_id) VALUES
('Dr. John Smith', 'Cardiologist', '1234567890', 1),
('Dr. Emily White', 'Neurologist', '2345678901', 2),
('Dr. Mark Lee', 'Orthopedic Surgeon', '3456789012', 3),
('Dr. Alice Brown', 'Pediatrician', '4567890123', 4),
('Dr. Robert Green', 'General Physician', '5678901234', 5);
