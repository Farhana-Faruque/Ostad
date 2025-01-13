CREATE TABLE Appointments(
    apt_id INT PRIMARY KEY,
    doctor_id INT,
    patient_id INT,
    apt_date DATE,
    apt_time TIME,
    doc_status VARCHAR(50),
    FOREIGN KEY Appointments(doctor_id) REFERENCES doctors(doctor_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY Appointments(patient_id) REFERENCES patients(patients_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

INSERT INTO Appointments (apt_id, doctor_id, patient_id, apt_date , apt_time, doc_status) VALUES
(1, 1, 1, '2024-12-22', '10:00:00', 'Confirmed'),
(2, 2, 2, '2024-12-23', '11:00:00', 'Pending'),
(3, 3, 3, '2024-12-24', '12:00:00', 'Confirmed'),
(4, 4, 4, '2024-12-25', '13:00:00', 'Cancelled'),
(5, 5, 5, '2024-12-26', '14:00:00', 'Confirmed');