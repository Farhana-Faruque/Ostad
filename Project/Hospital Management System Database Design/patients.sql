CREATE TABLE patients(
    patients_id INT PRIMARY KEY AUTO_INCREMENT,
    patients_name VARCHAR(100) NOT NULL,
    age INT,
    phone VARCHAR(15) NOT NULL,
    gender CHAR(1) 
);

INSERT INTO patients (patients_name, age, phone, gender) VALUES
('Alice Johnson', 30, '9876543210', 'F'),
('Bob Wilson', 45, '8765432109', 'M'),
('Charlie Davis', 25, '7654321098' , 'M'),
('Diana Evans', 40, '6543210987', 'F'),
('Ethan Hall', 35, '5432109876' , 'M' );
