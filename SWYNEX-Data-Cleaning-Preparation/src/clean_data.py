import pandas as pd

INPUT_FILE = "../data/raw/raw_dataset.csv"
OUTPUT_FILE = "../data/cleaned/cleaned_dataset.csv"
REPORT_FILE = "../reports/data_quality_report.csv"

# Load raw dataset
df = pd.read_csv(INPUT_FILE)
original_rows = len(df)

# Count issues before cleaning
missing_before = int(df.isna().sum().sum())
duplicates_before = int(df.duplicated().sum())

# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
)

# Remove leading/trailing spaces from text columns
text_columns = df.select_dtypes(include="object").columns
for column in text_columns:
    df[column] = df[column].str.strip()

# Standardize categorical values
df["gender"] = (
    df["gender"]
    .str.lower()
    .replace({"m": "Male", "male": "Male",
              "f": "Female", "female": "Female"})
)

df["city"] = (
    df["city"]
    .str.lower()
    .replace({"hyderabad": "Hyderabad",
              "secunderabad": "Secunderabad",
              "warangal": "Warangal"})
)

# Convert numeric columns
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["annual_income"] = pd.to_numeric(df["annual_income"], errors="coerce")
df["purchase_amount"] = pd.to_numeric(df["purchase_amount"], errors="coerce")

# Convert dates to a consistent format
df["purchase_date"] = pd.to_datetime(
    df["purchase_date"], errors="coerce", dayfirst=False
)

# Remove exact duplicate records
df = df.drop_duplicates()

# Handle missing numeric values with median
for column in ["age", "annual_income", "purchase_amount"]:
    df[column] = df[column].fillna(df[column].median())

# Handle missing categorical values
df["gender"] = df["gender"].fillna("Unknown")
df["city"] = df["city"].fillna("Unknown")

# Handle invalid/missing dates
df["purchase_date"] = df["purchase_date"].fillna(
    df["purchase_date"].mode()[0]
)

# Format dates consistently
df["purchase_date"] = df["purchase_date"].dt.strftime("%Y-%m-%d")

# Save cleaned data
df.to_csv(OUTPUT_FILE, index=False)

# Create quality report
missing_after = int(df.isna().sum().sum())
duplicates_after = int(df.duplicated().sum())

report = pd.DataFrame({
    "Issue": [
        "Missing values",
        "Duplicate records",
        "Incorrect/inconsistent data types",
        "Inconsistent categorical values"
    ],
    "Before": [
        missing_before,
        duplicates_before,
        "Multiple",
        "Multiple"
    ],
    "After": [
        missing_after,
        duplicates_after,
        "Standardized",
        "Standardized"
    ],
    "Action": [
        "Numeric median / categorical Unknown / date mode",
        "Removed exact duplicate rows",
        "Converted numeric and date columns",
        "Standardized Gender and City"
    ]
})

report.to_csv(REPORT_FILE, index=False)

print("Cleaning completed successfully.")
print("Original rows:", original_rows)
print("Final rows:", len(df))
print("Duplicates before:", duplicates_before)
print("Duplicates after:", duplicates_after)
print("Missing values before:", missing_before)
print("Missing values after:", missing_after)
print("Cleaned file:", OUTPUT_FILE)
