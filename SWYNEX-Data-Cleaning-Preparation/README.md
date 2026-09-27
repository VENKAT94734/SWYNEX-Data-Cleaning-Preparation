# SWYNEX Data Cleaning & Preparation

## Task
SWYNEX Internship - Task 1: Data Cleaning & Preparation

## Objective
Clean and prepare a public-style customer dataset for analysis by identifying and correcting:
- Missing values
- Duplicate records
- Incorrect data types
- Inconsistent categorical values
- Unnecessary whitespace
- Inconsistent date formats

## Dataset
The raw dataset is stored in `data/raw/raw_dataset.csv`.

It contains customer information including customer ID, name, gender, age, city, annual income, purchase date and purchase amount.

## Tools Used
- Python
- Pandas
- Jupyter Notebook
- CSV

## Cleaning Process
1. Loaded the raw CSV.
2. Inspected missing values, duplicates and data types.
3. Cleaned column names and whitespace.
4. Standardized Gender and City values.
5. Converted numeric columns to numeric data types.
6. Converted Purchase Date to a consistent date format.
7. Removed duplicate records.
8. Handled missing numeric values using median imputation.
9. Handled missing categorical values using `Unknown`.
10. Saved the cleaned dataset.
11. Generated a data-quality report.

## Project Structure

```text
SWYNEX-Data-Cleaning-Preparation/
├── data/
│   ├── raw/
│   │   └── raw_dataset.csv
│   └── cleaned/
│       └── cleaned_dataset.csv
├── notebooks/
│   └── data_cleaning.ipynb
├── reports/
│   └── data_quality_report.csv
├── src/
│   └── clean_data.py
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

Open a terminal in the project folder and install dependencies:

```bash
pip install -r requirements.txt
```

Then enter the `src` folder:

```bash
cd src
python clean_data.py
```

The cleaned dataset will be generated at:

`data/cleaned/cleaned_dataset.csv`

The quality report will be generated at:

`reports/data_quality_report.csv`

## Result
The project produces a cleaned dataset suitable for further data analysis while documenting the quality issues and cleaning actions.
