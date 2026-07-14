import pandas as pd
import numpy as np

# ============================================
# Load Dataset
# ============================================

df = pd.read_csv("D:\\analytic_project\\Healthcare_ETL_Pipeline\\data\\healthcare_noisy.csv")

print("=" * 60)
print("STARTING DATA CLEANING")
print("=" * 60)

print(f"Rows Before Cleaning : {len(df)}")

# ============================================
# 1. Handle Missing Values
# ============================================

# Medical Condition -> Mode
df["Medical Condition"] = df["Medical Condition"].fillna(
    df["Medical Condition"].mode()[0]
)

# Insurance Provider -> Unknown (Business Rule)
df["Insurance Provider"] = df["Insurance Provider"].fillna(
    "Unknown"
)

# Billing Amount -> Median
df["Billing Amount"] = df["Billing Amount"].fillna(
    df["Billing Amount"].median()
)

print("✓ Missing values handled")

# ============================================
# 2. Remove Duplicate Rows
# ============================================

before = len(df)

df = df.drop_duplicates()

after = len(df)

print(f"✓ Removed {before-after} duplicate rows")

# ============================================
# 3. Standardize Gender
# ============================================

df["Gender"] = (
    df["Gender"]
    .astype(str)
    .str.strip()
    .str.title()
)

print("✓ Gender standardized")

# ============================================
# 4. Standardize Admission Type
# ============================================

df["Admission Type"] = (
    df["Admission Type"]
    .astype(str)
    .str.strip()
    .str.title()
)

print("✓ Admission Type standardized")

# ============================================
# 5. Validate Blood Types
# ============================================

valid_blood = [
    "A+", "A-",
    "B+", "B-",
    "AB+", "AB-",
    "O+", "O-"
]

df["Blood Type"] = np.where(
    df["Blood Type"].isin(valid_blood),
    df["Blood Type"],
    "Unknown"
)

print("✓ Invalid Blood Types corrected")

# ============================================
# 6. Remove Invalid Ages
# ============================================

before = len(df)

df = df[
    (df["Age"] >= 0) &
    (df["Age"] <= 120)
]

after = len(df)

print(f"✓ Removed {before-after} invalid age rows")

# ============================================
# 7. Handle Billing Outliers
# ============================================

upper_limit = df["Billing Amount"].quantile(0.99)

df["Billing Amount"] = np.where(
    df["Billing Amount"] > upper_limit,
    upper_limit,
    df["Billing Amount"]
)

print("✓ Billing outliers capped")

# ============================================
# 8. Standardize Dates
# ============================================

# Since we removed mixed-date injection,
# pandas can parse dates normally.

df["Date of Admission"] = pd.to_datetime(
    df["Date of Admission"],
    errors="coerce"
)

df["Discharge Date"] = pd.to_datetime(
    df["Discharge Date"],
    errors="coerce"
)

# Admission Date is mandatory
df = df[df["Date of Admission"].notna()]

# Format dates
df["Date of Admission"] = (
    df["Date of Admission"]
    .dt.strftime("%Y-%m-%d")
)

# Keep missing discharge dates blank
df["Discharge Date"] = (
    df["Discharge Date"]
    .apply(lambda x: x.strftime("%Y-%m-%d") if pd.notna(x) else "")
)

print("✓ Dates standardized")

# ============================================
# 9. Final Data Quality Check
# ============================================

print("\nFinal Data Quality Report")
print("-" * 40)

print("Missing Values")
print(df.isnull().sum())

print("\nDuplicate Rows :", df.duplicated().sum())

print("\nRows After Cleaning :", len(df))

# ============================================
# 10. Save Clean Dataset
# ============================================

df.to_csv(
    "D:\\analytic_project\\Healthcare_ETL_Pipeline\\data\\healthcare_cleaned.csv",
    index=False
)

print("\n✓ Clean dataset saved successfully")

print("=" * 60)
print("DATA CLEANING COMPLETED")
print("=" * 60)