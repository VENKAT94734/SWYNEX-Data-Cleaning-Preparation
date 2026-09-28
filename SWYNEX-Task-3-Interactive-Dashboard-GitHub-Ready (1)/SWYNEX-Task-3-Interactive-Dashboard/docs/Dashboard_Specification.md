# SWYNEX Task 3 — Dashboard Specification

## Dashboard title
Customer Sales & Purchase Analytics Dashboard

## Data source
`data/dashboard_dataset.csv`

## KPI cards
1. Total Customers → `[Total Customers]`
2. Total Purchase → `[Total Purchase]`
3. Average Purchase → `[Average Purchase]`
4. Average Annual Income → `[Average Annual Income]`

## Visuals
### 1. Purchase Amount by City
- Visual: Clustered column chart
- Axis: City
- Values: Total Purchase

### 2. Customer Distribution by Gender
- Visual: Donut chart
- Legend: Gender
- Values: Total Customers

### 3. Purchase Amount by Gender
- Visual: Clustered column chart
- Axis: Gender
- Values: Total Purchase

### 4. Monthly Purchase Trend
- Visual: Line chart
- Axis: Purchase_Date → Month
- Values: Total Purchase

### 5. Annual Income vs Purchase Amount
- Visual: Scatter chart
- X-axis: Annual_Income
- Y-axis: Purchase_Amount
- Details: Customer_ID

### 6. Top 5 Customers
- Visual: Horizontal bar chart
- Axis: Customer_Name
- Values: Purchase_Amount
- Visual filter: Top N = 5 by Purchase_Amount

## Slicers
- City
- Gender
- Purchase_Date
- Age

## Recommended layout
Top: dashboard title + 4 KPI cards
Second row: slicers
Third row: City purchase + Gender distribution
Fourth row: Monthly trend + Gender purchase
Bottom: Income vs Purchase scatter + Top 5 customers

## Interaction
Enable cross-filtering between visuals. Selecting a city, gender, date or age should update KPI cards and charts.
