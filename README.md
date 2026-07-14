# 🏥 Healthcare ETL & Analytics Pipeline

An end-to-end healthcare data ETL (Extract, Transform, Load) and analytics project — from raw data ingestion through cleaning, validation, MySQL storage, and an interactive Power BI dashboard.

The source dataset already contained some real-world data quality issues (duplicate records, negative billing values, inconsistent name casing). To build a more complete pipeline demo, a small set of additional synthetic issues (nulls, invalid categories, outliers, mixed date formats) was deliberately layered on top — clearly separated from the real issues in the code and documented below.

---

## 📌 Project Overview

Raw operational data — healthcare or otherwise — rarely arrives clean. This project builds a repeatable pipeline to:

- Ingest raw healthcare records
- Detect and quantify data quality issues (nulls, duplicates, invalid values, outliers, format inconsistencies)
- Clean and standardize the data using defined business rules
- Load the cleaned dataset into MySQL for structured storage and SQL-based analysis
- Visualize key business insights in Power BI

---

## 🛠 Tech Stack

Python · Pandas · NumPy · MySQL · SQL · Power BI

---

## 📂 Project Structure

```text
Healthcare-ETL-Analytics-Pipeline
│
├── data
│   ├── healthcare_raw.csv          # source data
|   ├── healthcare_noisy.csv        # noisy data          
│   └── healthcare_cleaned.csv      # final cleaned output
│
├── scripts
│   ├── inject_noise.py          # adds controlled synthetic data issues
|   ├── validate_data.py                                # inspects the data
│   └── clean_pipeline.py        # full cleaning + validation pipeline
│
├── sql
│   ├── schema.sql                  # MySQL table definition
│   └── analysis_queries.sql        # business analysis queries
│
├── powerbi
│   └── Healthcare_Dashboard.pbix
|   ├── dashboard_page1.png
│   └── dashboard_page2.png   
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 ETL Workflow

```text
Raw Dataset (real + synthetic data issues)
          │
          ▼
Ingestion (Python / Pandas)
          │
          ▼
Validation & Cleaning
  • Null handling
  • Duplicate removal
  • Business-rule checks (negative billing, invalid age)
  • Category standardization (Blood Type, Gender, Admission Type)
  • Date format standardization
  • Outlier detection (IQR method, flagged not deleted)
          │
          ▼
Cleaned Dataset
          │
          ▼
MySQL (structured storage + SQL analysis)
          │
          ▼
Power BI Dashboard (built on the processed dataset)
```

---

## ✅ Data Quality Results

Actual output from the pipeline, run on 55,500 source records:

| Issue | Records Affected | Action Taken |
|---|---|---|
| Duplicate rows | 422 | Removed |
| Missing Billing Amount | 1665 | Imputed with column median |
| Missing Medical Condition | 1665 | Filled as "Unknown" |
| Missing Insurance Provider | 1664 | Filled as "Unknown" |
| Inconsistent Gender casing | 1110 | Standardized |
| Negative Billing Amount | 105 | Corrected to absolute value, flagged for review |
| Invalid Age (<0 or >120) | 10 | Removed (not recoverable) |
| Invalid Blood Type values | 15 | Set to "Unknown" |
| Mixed date formats | 1,110 | Parsed and standardized to YYYY-MM-DD |
| Billing Amount outliers (IQR) | 20 | Flagged for analyst review |

**Result: 55,500 → 55,068 clean, validated records** (432 rows removed: 422 duplicates + 10 unrecoverable invalid-age rows).

Full row-level log: [`reports/data_quality_report.csv`](reports/data_quality_report.csv)

---

## 📊 Dashboard

Built in Power BI on the cleaned dataset:

- Total Patients, Total Revenue, Average Billing Amount, Average Patient Age
- Patients by Medical Condition
- Monthly Admission Trends
- Revenue by Insurance Provider
- Admission Type Distribution
- Blood Type & Medication Distribution
- Test Results breakdown with interactive filters

### Preview
![dashboard1](https://github.com/Vishvapriya-24/Healthcare-ETL-Analytics-Pipeline/blob/c0a9a25c5beba31d0bbd960a7aacc268526c17ee/powerbi/Overall_Dashboard.png)

![dashboard2](https://github.com/Vishvapriya-24/Healthcare-ETL-Analytics-Pipeline/blob/c0a9a25c5beba31d0bbd960a7aacc268526c17ee/powerbi/Detailed_Dashboard.png)


---

## 💡 Business Questions This Answers

- Which medical conditions are most common, and most costly?
- Which insurance providers account for the highest billing volume?
- How do patient admissions trend over time?
- Which medications are most frequently prescribed?
- How is billing amount distributed across admission types?

---

## 🚀 How to Run

```bash
git clone https://github.com/Vishvapriya-24/Healthcare-ETL-Analytics-Pipeline.git
pip install -r requirements.txt

python scripts/01_inject_noise.py
python scripts/02_clean_pipeline.py
```

Then load the cleaned data into MySQL:
```bash
mysql -u root -p < sql/schema.sql
# import data/healthcare_cleaned.csv into the created table
```

Run `sql/analysis_queries.sql` for the SQL-based analysis, and open `powerbi/Healthcare_Dashboard.pbix` to view the dashboard.

---

## ⚠️ Known Limitation

The Power BI dashboard is currently built directly on the cleaned CSV output rather than a live MySQL connection — I ran into connector setup issues when connecting Power BI to MySQL directly. MySQL is fully used for structured storage and the SQL analysis queries in this project; wiring Power BI to query MySQL live (instead of the static export) is a planned next step.

---

## 📈 Skills Demonstrated

Data Cleaning · ETL Pipeline Development · Data Validation · SQL Querying · MySQL · Business Intelligence · Data Visualization · Power BI · Python Data Processing

---

## 👩‍💻 Author

**Vishvapriya M**
[LinkedIn](https://www.linkedin.com/in/vishvapriya-murugan-973a03315/) · [GitHub](https://github.com/Vishvapriya-24)

---

⭐ If you found this project useful, consider giving it a star!
