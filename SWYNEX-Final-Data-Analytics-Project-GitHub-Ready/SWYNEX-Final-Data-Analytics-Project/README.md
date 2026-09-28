# SWYNEX Task 4 — Final Data Analytics Project

This repository combines the SWYNEX internship Tasks 1–3 into a complete analytics case study.

> **Dataset note:** The included dataset is a demonstration dataset created for this project. If the internship requires a verifiable external public dataset, replace `data/raw/raw_dataset.csv` with the required public dataset and rerun the workflow.

## Workflow
**Data Cleaning → EDA → Interactive Dashboard → Business Insights**

## Problem Statement
Raw customer data may contain duplicate records, inconsistent categories, invalid numeric values and inconsistent dates. This project prepares the data and communicates the resulting patterns through dashboard-ready analytics.

## Contents
- `data/` — raw and cleaned datasets
- `notebooks/` — analysis notebook
- `dashboard/` — Power BI DAX, theme and dashboard specification
- `reports/` — quality report and business insights
- `docs/` — final case study
- `README.md` — project documentation

## Tools
Python, Pandas, NumPy, Matplotlib, Jupyter Notebook, Power BI, DAX and GitHub.

## Power BI
Import `data/cleaned/cleaned_dataset.csv`, create the measures from `dashboard/DAX_Measures.dax`, and follow `dashboard/dashboard_specification.md`.

## Reproduce
```bash
pip install -r requirements.txt
jupyter notebook
```

## Final Deliverable
The project covers the problem statement, dataset information, cleaning, analysis, dashboard design and key business insights required for SWYNEX Task 4.
