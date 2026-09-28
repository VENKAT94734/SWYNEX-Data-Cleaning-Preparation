# SWYNEX Task 3 — Interactive Dashboard

## Internship Task
**Task 3: Interactive Dashboard**

### Objective
Build a professional interactive dashboard from the analyzed customer dataset and communicate the main findings through KPIs, charts and interactive filters.

## Tool
**Microsoft Power BI Desktop**

This repository is Power BI-ready. The actual `.pbix` report must be created/saved from Power BI Desktop after importing the supplied CSV and applying the included measures and theme.

## Dataset
`data/dashboard_dataset.csv`

The dataset follows the same customer-analysis schema used in the earlier internship work:

- Customer ID
- Customer Name
- Gender
- Age
- City
- Annual Income
- Purchase Date
- Purchase Amount

## Dashboard components

### KPIs
- Total Customers
- Total Purchase Amount
- Average Purchase Amount
- Average Annual Income

### Charts
- Purchase Amount by City
- Customer Distribution by Gender
- Purchase Amount by Gender
- Monthly Purchase Trend
- Annual Income vs Purchase Amount
- Top 5 Customers by Purchase Amount

### Filters
- City
- Gender
- Purchase Date
- Age

## Power BI setup

1. Open **Power BI Desktop**.
2. Select **Get Data → Text/CSV**.
3. Select `data/dashboard_dataset.csv`.
4. Load the table and rename it to `CustomerData`.
5. Set data types:
   - Customer_ID → Whole Number
   - Customer_Name → Text
   - Gender → Text
   - Age → Whole Number
   - City → Text
   - Annual_Income → Whole Number
   - Purchase_Date → Date
   - Purchase_Amount → Whole Number
6. Open **Modeling → New Measure**.
7. Add the measures from `powerbi/DAX_Measures.dax`.
8. Import `powerbi/PowerBI_Theme.json` using **View → Themes → Browse for themes**.
9. Build the visuals according to `docs/Dashboard_Specification.md`.
10. Add the four slicers and test cross-filtering.
11. Save the finished report as:

`SWYNEX-Task-3-Interactive-Dashboard.pbix`

## Suggested dashboard design

```text
┌──────────────────────────────────────────────────────────────┐
│       CUSTOMER SALES & PURCHASE ANALYTICS                   │
├────────────┬────────────┬────────────┬──────────────────────┤
│ Customers  │ Total      │ Avg        │ Avg Annual Income   │
│            │ Purchase   │ Purchase   │                     │
├──────────────────────────────────────────────────────────────┤
│ City | Gender | Purchase Date | Age                         │
├─────────────────────────────┬────────────────────────────────┤
│ Purchase by City            │ Customer Distribution          │
│                             │ by Gender                      │
├─────────────────────────────┼────────────────────────────────┤
│ Monthly Purchase Trend      │ Purchase by Gender             │
├─────────────────────────────┴────────────────────────────────┤
│ Annual Income vs Purchase Amount                             │
├──────────────────────────────────────────────────────────────┤
│ Top 5 Customers                                               │
└──────────────────────────────────────────────────────────────┘
```

## Files

```text
SWYNEX-Task-3-Interactive-Dashboard/
├── data/
│   └── dashboard_dataset.csv
├── docs/
│   └── Dashboard_Specification.md
├── powerbi/
│   ├── DAX_Measures.dax
│   └── PowerBI_Theme.json
├── preview/
│   └── dashboard_wireframe.svg
├── reports/
├── README.md
└── requirements.txt
```

## Submission evidence

After creating the dashboard in Power BI:

- Take a screenshot showing the complete dashboard.
- Take one screenshot with a filter selected to demonstrate interactivity.
- Upload the `.pbix` file if permitted by your internship.
- Push this repository to GitHub.

## Important note

The supplied CSV is a dashboard-ready demonstration dataset following the same customer schema used for the internship tasks. If the internship requires a verifiable external public dataset, replace this CSV with the actual cleaned public dataset from Task 1 before final submission.

## Internship
**Organization:** SWYNEX Technologies  
**Task 1:** Data Cleaning & Preparation  
**Task 2:** Exploratory Data Analysis  
**Task 3:** Interactive Dashboard
