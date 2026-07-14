CREATE DATABASE healthcare_etl;

USE healthcare_etl;

CREATE TABLE healthcare_records (

    patient_id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100),

    age INT,

    gender VARCHAR(20),

    blood_type VARCHAR(10),

    medical_condition VARCHAR(100),

    admission_date DATE,

    doctor VARCHAR(100),

    hospital VARCHAR(150),

    insurance_provider VARCHAR(100),

    billing_amount DECIMAL(12,2),

    room_number INT,

    admission_type VARCHAR(50),

    discharge_date DATE,

    medication VARCHAR(100),

    test_results VARCHAR(50)

);