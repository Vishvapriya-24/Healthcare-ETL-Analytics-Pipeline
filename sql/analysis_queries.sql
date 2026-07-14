SELECT COUNT(*) AS total_patients
FROM healthcare_records;


SELECT
ROUND(AVG(billing_amount),2) AS average_bill
FROM healthcare_records;


SELECT
ROUND(SUM(billing_amount),2) AS total_revenue
FROM healthcare_records;


SELECT
medical_condition,
COUNT(*) AS total_patients
FROM healthcare_records
GROUP BY medical_condition
ORDER BY total_patients DESC;


SELECT
insurance_provider,
ROUND(SUM(billing_amount),2) AS revenue
FROM healthcare_records
GROUP BY insurance_provider
ORDER BY revenue DESC;


SELECT
admission_type,
COUNT(*) AS patients
FROM healthcare_records
GROUP BY admission_type
ORDER BY patients DESC;


SELECT
blood_type,
COUNT(*) AS patients
FROM healthcare_records
GROUP BY blood_type
ORDER BY patients DESC;


SELECT
medical_condition,
ROUND(AVG(age),1) AS average_age
FROM healthcare_records
GROUP BY medical_condition
ORDER BY average_age DESC;


SELECT
name,
medical_condition,
hospital,
billing_amount
FROM healthcare_records
ORDER BY billing_amount DESC
LIMIT 10;


SELECT
MONTH(admission_date) AS month,
COUNT(*) AS patients
FROM healthcare_records
GROUP BY MONTH(admission_date)
ORDER BY month;


SELECT
test_results,
COUNT(*) AS patients
FROM healthcare_records
GROUP BY test_results;


SELECT
hospital,
COUNT(*) AS patients
FROM healthcare_records
GROUP BY hospital
ORDER BY patients DESC
LIMIT 10;



SELECT
medication,
COUNT(*) AS prescriptions
FROM healthcare_records
GROUP BY medication
ORDER BY prescriptions DESC;


SELECT
admission_type,
ROUND(AVG(billing_amount),2) AS average_bill
FROM healthcare_records
GROUP BY admission_type;


SELECT
insurance_provider,
ROUND(AVG(billing_amount),2) AS average_bill
FROM healthcare_records
GROUP BY insurance_provider
ORDER BY average_bill DESC;