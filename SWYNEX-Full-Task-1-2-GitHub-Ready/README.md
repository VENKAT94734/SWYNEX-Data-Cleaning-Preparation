# SWYNEX Data Cleaning & Exploratory Data Analysis

## Internship Tasks 1 & 2

This repository contains the complete work for the SWYNEX internship:

- **Task 1:** Data Cleaning & Preparation
- **Task 2:** Exploratory Data Analysis

## Task 1 — Data Cleaning & Preparation

The raw customer dataset was inspected and cleaned for missing values, duplicate records, incorrect data types, inconsistent categorical values, whitespace, and inconsistent date formats.

### Task 1 output
- `data/cleaned/cleaned_dataset.csv`
- `reports/data_quality_report.csv`
- `notebooks/data_cleaning.ipynb`
- `src/clean_data.py`

## Task 2 — Exploratory Data Analysis

Task 2 uses the cleaned dataset produced in Task 1.

The EDA includes:

- Dataset overview
- Descriptive statistics
- Gender distribution
- City distribution
- Age distribution
- Annual income distribution
- Purchase amount distribution
- Highest-spending customers
- City-wise average purchase
- Gender-wise average purchase
- Income vs purchase correlation
- Monthly purchase trend
- IQR-based anomaly detection
- Eight documented data-driven insights

### Task 2 output
- `notebooks/exploratory_data_analysis_executed.ipynb`
- `reports/eda_summary.csv`
- `visualizations/`

## Project Structure

```text
SWYNEX-Full-Task-1-2/
├── data/
│   ├── raw/
│   │   └── raw_dataset.csv
│   └── cleaned/
│       └── cleaned_dataset.csv
├── notebooks/
│   ├── exploratory_data_analysis_executed.ipynb
│   └── data_cleaning.ipynb
├── reports/
│   ├── data_quality_report.csv
│   └── eda_summary.csv
├── visualizations/
├── src/
│   └── clean_data.py
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

```bash
pip install -r requirements.txt
```

For Task 1:

```bash
cd src
python clean_data.py
```

For Task 2:

```bash
jupyter notebook
```

Open:

`notebooks/exploratory_data_analysis_executed.ipynb`

## Key Result

The executed Task 2 notebook contains the analysis outputs and visualizations, so the reviewer can inspect the results directly without having to execute the notebook first.

## Important Note

The insights are observations from this sample dataset. They should not be generalized to a larger population without a larger and representative dataset.

## Internship

**Organization:** SWYNEX Technologies  
**Task 1:** Data Cleaning & Preparation  
**Task 2:** Exploratory Data Analysis
