import pandas as pd

INPUT_FILE = "../data/raw/raw_dataset.csv"
OUTPUT_FILE = "../data/cleaned/cleaned_dataset.csv"
REPORT_FILE = "../reports/data_quality_report.csv"

df = pd.read_csv(INPUT_FILE)
missing_before = int(df.isna().sum().sum())
duplicates_before = int(df.duplicated().sum())

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

df["gender"] = df["gender"].str.lower().replace({
    "m": "Male", "male": "Male", "f": "Female", "female": "Female"
})
df["city"] = df["city"].str.lower().replace({
    "hyderabad": "Hyderabad",
    "secunderabad": "Secunderabad",
    "warangal": "Warangal"
})

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["annual_income"] = pd.to_numeric(df["annual_income"], errors="coerce")
df["purchase_amount"] = pd.to_numeric(df["purchase_amount"], errors="coerce")
df["purchase_date"] = pd.to_datetime(df["purchase_date"], errors="coerce")

df = df.drop_duplicates()

for column in ["age", "annual_income", "purchase_amount"]:
    df[column] = df[column].fillna(df[column].median())

df["gender"] = df["gender"].fillna("Unknown")
df["city"] = df["city"].fillna("Unknown")
df["purchase_date"] = df["purchase_date"].fillna(df["purchase_date"].mode()[0])
df["purchase_date"] = df["purchase_date"].dt.strftime("%Y-%m-%d")

df.to_csv(OUTPUT_FILE, index=False)

report = pd.DataFrame({
    "Issue": ["Missing values", "Duplicate records",
              "Incorrect data types", "Inconsistent categorical values"],
    "Before": [missing_before, duplicates_before, "Multiple", "Multiple"],
    "After": [int(df.isna().sum().sum()), int(df.duplicated().sum()),
              "Standardized", "Standardized"],
    "Action": [
        "Median / Unknown / date mode",
        "Removed duplicate rows",
        "Converted numeric and date columns",
        "Standardized Gender and City"
    ]
})
report.to_csv(REPORT_FILE, index=False)

print("Cleaning completed successfully.")
print("Original rows:", len(pd.read_csv(INPUT_FILE)))
print("Final rows:", len(df))
