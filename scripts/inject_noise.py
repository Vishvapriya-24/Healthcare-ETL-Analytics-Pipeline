
import pandas as pd
import numpy as np

df = pd.read_csv("D:\\analytic_project\\Healthcare_ETL_Pipeline\\data\\healthcare_dataset.csv")
print(df.shape)

np.random.seed(42)

missing_cols = [
    "Medical Condition",
    "Insurance Provider",
    "Billing Amount"
]

for col in missing_cols:
    idx = np.random.choice(
        df.index,
        size=int(len(df) * 0.03),
        replace=False
    )

    df.loc[idx, col] = np.nan


gender_idx = np.random.choice(
    df.index,
    size=int(len(df) * 0.02),
    replace=False
)

for i in gender_idx:

    value = str(df.at[i, "Gender"])

    df.at[i, "Gender"] = np.random.choice([
        value.lower(),
        value.upper(),
        value.swapcase()
    ])

admission_idx = np.random.choice(
    df.index,
    size=int(len(df) * 0.02),
    replace=False
)

for i in admission_idx:

    value = str(df.at[i, "Admission Type"])

    df.at[i, "Admission Type"] = np.random.choice([
        value.lower(),
        value.upper(),
        value.swapcase()
    ])

blood_idx = np.random.choice(
    df.index,
    size=15,
    replace=False
)

invalid_values = [
    "X+",
    "Unknown",
    "",
    "A++"
]

for i in blood_idx:

    df.at[i, "Blood Type"] = np.random.choice(invalid_values)


bill_idx = np.random.choice(
    df.index,
    size=20,
    replace=False
)

outliers = [
    500000,
    650000,
    750000,
    999999
]

for i in bill_idx:

    df.at[i, "Billing Amount"] = np.random.choice(outliers)



age_idx = np.random.choice(
    df.index,
    size=10,
    replace=False
)

ages = [
    -5,
    -10,
    135,
    200
]

for i in age_idx:

    df.at[i, "Age"] = np.random.choice(ages)


# date_idx = np.random.choice(
#     df.index,
#     size=int(len(df) * 0.02),
#     replace=False
# )

# for i in date_idx:

#     date = pd.to_datetime(df.at[i, "Date of Admission"])

#     df.at[i, "Date of Admission"] = date.strftime("%d/%m/%Y")


df.to_csv(
    "D:\\analytic_project\\Healthcare_ETL_Pipeline\\data\\healthcare_noisy.csv",
    index=False
)

print("Noisy dataset created successfully!")