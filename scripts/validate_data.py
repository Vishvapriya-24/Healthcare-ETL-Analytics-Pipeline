import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("D:\\analytic_project\\Healthcare_ETL_Pipeline\\data\\healthcare_noisy.csv")

print("=" * 60)
print("HEALTHCARE DATA QUALITY REPORT")
print("=" * 60)

print(f"\nTotal Rows    : {len(df)}")
print(f"Total Columns : {len(df.columns)}")

# -----------------------------
# Missing Values
# -----------------------------
print("\n" + "=" * 60)
print("1. MISSING VALUES")
print("=" * 60)

missing = df.isnull().sum()
missing = missing[missing > 0]

if len(missing) == 0:
    print("No Missing Values Found")
else:
    print(missing)

# -----------------------------
# Duplicate Rows
# -----------------------------
print("\n" + "=" * 60)
print("2. DUPLICATE ROWS")
print("=" * 60)

duplicates = df.duplicated().sum()
print(f"Duplicate Rows : {duplicates}")

# -----------------------------
# Invalid Age
# -----------------------------
print("\n" + "=" * 60)
print("3. INVALID AGE")
print("=" * 60)

invalid_age = df[(df["Age"] < 0) | (df["Age"] > 120)]

print(f"Invalid Age Rows : {len(invalid_age)}")

# -----------------------------
# Invalid Blood Type
# -----------------------------
print("\n" + "=" * 60)
print("4. INVALID BLOOD TYPES")
print("=" * 60)

valid_blood = [
    "A+","A-",
    "B+","B-",
    "AB+","AB-",
    "O+","O-"
]

invalid_blood = df[~df["Blood Type"].isin(valid_blood)]

print(f"Invalid Blood Types : {len(invalid_blood)}")

# -----------------------------
# Billing Amount Outliers
# -----------------------------
print("\n" + "=" * 60)
print("5. BILLING OUTLIERS")
print("=" * 60)

outliers = df[df["Billing Amount"] > 100000]

print(f"Extreme Billing Amounts : {len(outliers)}")

# -----------------------------
# Gender Validation
# -----------------------------
print("\n" + "=" * 60)
print("6. GENDER VALUES")
print("=" * 60)

print(df["Gender"].value_counts(dropna=False))

# -----------------------------
# Admission Type Validation
# -----------------------------
print("\n" + "=" * 60)
print("7. ADMISSION TYPE VALUES")
print("=" * 60)

print(df["Admission Type"].value_counts(dropna=False))

# -----------------------------
# Date Validation
# -----------------------------
print("\n" + "=" * 60)
print("8. DATE FORMAT CHECK")
print("=" * 60)

parsed = pd.to_datetime(
    df["Date of Admission"],
    errors="coerce",
    dayfirst=True
)

invalid_dates = parsed.isna().sum()

print(f"Invalid Date Formats : {invalid_dates}")

# -----------------------------
# Summary
# -----------------------------
print("\n" + "=" * 60)
print("DATA QUALITY SUMMARY")
print("=" * 60)

print(f"""
Missing Values            : {df.isnull().sum().sum()}
Duplicate Rows            : {duplicates}
Invalid Ages              : {len(invalid_age)}
Invalid Blood Types       : {len(invalid_blood)}
Billing Outliers          : {len(outliers)}
Invalid Dates             : {invalid_dates}
""")

print("=" * 60)