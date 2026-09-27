# SWYNEX Data Cleaning & Preparation

## SWYNEX Internship — Task 1

### Project Overview

This project was completed as part of the **SWYNEX Internship Task 1: Data Cleaning & Preparation**.

The objective of this project is to identify, clean, and prepare a raw customer dataset for further data analysis using **Python and Pandas**.

The project demonstrates a practical data-cleaning workflow involving missing values, duplicate records, incorrect data types, inconsistent categorical values, whitespace, and inconsistent date formats.

---

## Objective

The main objectives of this project are to:

* Identify missing values
* Detect and remove duplicate records
* Identify and correct incorrect data types
* Standardize inconsistent categorical values
* Remove unnecessary whitespace
* Standardize date formats
* Validate the cleaned dataset
* Export the final cleaned dataset
* Generate a data-quality report

---

## Dataset Description

The dataset contains customer-related information, including:

| Column            | Description                  |
| ----------------- | ---------------------------- |
| `Customer_ID`     | Unique customer identifier   |
| `Customer_Name`   | Customer name                |
| `Gender`          | Customer gender              |
| `Age`             | Customer age                 |
| `City`            | Customer city                |
| `Annual_Income`   | Customer annual income       |
| `Purchase_Date`   | Date of purchase             |
| `Purchase_Amount` | Amount spent by the customer |

The raw dataset intentionally contains several data-quality issues to demonstrate the cleaning process.

---

## Data Quality Issues Identified

The following issues were identified in the raw dataset:

### 1. Missing Values

Some records contain missing values in fields such as:

* Age
* Gender
* Annual Income
* Purchase Date

These missing values were identified and appropriately handled during preprocessing.

### 2. Duplicate Records

Duplicate records were identified using Pandas' `duplicated()` function.

Duplicate records were removed before creating the final dataset.

### 3. Incorrect Data Types

Some numeric fields were stored as text.

For example:

```text
Annual_Income
Age
Purchase_Amount
```

These columns were converted into appropriate numeric data types.

### 4. Inconsistent Gender Values

The raw dataset contains variations such as:

```text
Male
male
M
Female
female
F
```

These values were standardized to:

```text
Male
Female
```

### 5. Inconsistent City Values

City names appeared in different formats, such as:

```text
Hyderabad
HYDERABAD
 Hyderabad
Hyderabad
```

These values were standardized to consistent city names.

### 6. Inconsistent Date Formats

Dates appeared in different formats, including:

```text
2026-01-05
05/01/2026
2026/01/08
11-01-2026
```

The dates were converted into a consistent format:

```text
YYYY-MM-DD
```

### 7. Unnecessary Whitespace

Leading and trailing spaces were removed from text fields to improve consistency.

---

## Tools and Technologies

The following technologies were used:

* **Python**
* **Pandas**
* **NumPy**
* **Jupyter Notebook**
* **CSV**
* **VS Code**
* **Git & GitHub**

---

## Data Cleaning Process

The following workflow was followed:

```text
Raw Dataset
     ↓
Load Dataset
     ↓
Initial Data Inspection
     ↓
Check Missing Values
     ↓
Check Duplicate Records
     ↓
Check Data Types
     ↓
Check Inconsistent Values
     ↓
Clean Text and Column Names
     ↓
Standardize Categorical Values
     ↓
Convert Data Types
     ↓
Handle Missing Values
     ↓
Remove Duplicate Records
     ↓
Standardize Dates
     ↓
Validate Cleaned Dataset
     ↓
Export Cleaned Dataset
```

---

## Cleaning Methodology

### Missing Values

Numerical missing values were handled using median-based imputation where appropriate.

Categorical missing values were replaced with:

```text
Unknown
```

Missing dates were handled using the available valid date information.

### Duplicate Records

Exact duplicate rows were identified and removed.

### Numerical Data

The following fields were converted to appropriate numeric formats:

```text
Age
Annual_Income
Purchase_Amount
```

Invalid numerical values were converted to missing values before being handled appropriately.

### Categorical Data

Gender and city values were standardized to ensure consistency.

### Date Data

Purchase dates were converted into a consistent date format.

---

## Project Structure

```text
SWYNEX-Data-Cleaning-Preparation/
│
├── data/
│   ├── raw/
│   │   └── raw_dataset.csv
│   │
│   └── cleaned/
│       └── cleaned_dataset.csv
│
├── notebooks/
│   └── data_cleaning.ipynb
│
├── reports/
│   └── data_quality_report.csv
│
├── src/
│   └── clean_data.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Files Description

### `data/raw/raw_dataset.csv`

Contains the original raw dataset before cleaning.

### `data/cleaned/cleaned_dataset.csv`

Contains the final cleaned dataset prepared for further analysis.

### `notebooks/data_cleaning.ipynb`

Contains the step-by-step data inspection, cleaning, and validation process.

### `src/clean_data.py`

Contains the reusable Python script used to clean and prepare the dataset.

### `reports/data_quality_report.csv`

Contains a summary of the identified data-quality issues and the cleaning actions performed.

### `requirements.txt`

Contains the Python libraries required to run the project.

---

## How to Run the Project

### Step 1 — Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/SWYNEX-Data-Cleaning-Preparation.git
```

### Step 2 — Open the project

```bash
cd SWYNEX-Data-Cleaning-Preparation
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Run the cleaning script

```bash
cd src
python clean_data.py
```

The cleaned dataset will be generated at:

```text
data/cleaned/cleaned_dataset.csv
```

The data-quality report will be generated at:

```text
reports/data_quality_report.csv
```

---

## Validation

After cleaning, the dataset was validated by checking:

* Missing values
* Duplicate records
* Data types
* Categorical consistency
* Date consistency
* Final dataset structure

The validation process ensures that the cleaned dataset is suitable for further analysis.

---

## Results

The data-cleaning process successfully:

* Identified missing values
* Removed duplicate records
* Corrected numerical data types
* Standardized gender values
* Standardized city values
* Standardized date formats
* Removed unnecessary whitespace
* Generated a cleaned dataset
* Generated a data-quality report

---

## Conclusion

This project demonstrates a complete practical workflow for **data cleaning and preparation using Python and Pandas**.

The raw customer dataset was inspected, cleaned, validated, and converted into a structured dataset suitable for further data analysis.

The project also demonstrates how data-quality issues can affect analysis and why proper preprocessing is an important step before performing statistical analysis, visualization, or machine-learning tasks.

---

## Internship Task

**Organization:** SWYNEX Technologies

**Task:** Task 1 — Data Cleaning & Preparation

**Domain:** Data Analysis / Python

**Repository:** `SWYNEX-Data-Cleaning-Preparation`

---

## Author

**Venkat V**

B.Tech — Computer Science / Artificial Intelligence & Machine Learning
