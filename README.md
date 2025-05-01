# Data_analyst_task_7

------------------------------------------Sales Summary from SQLite using Python-------------------------------------------------

## Overview
This task involves creating a simple SQLite database and using Python to generate a basic sales summary, including total quantities and revenues for each product.

## Features
- Uses `sqlite3` to manage a local database.
- Executes SQL queries using Python.
- Displays results in terminal and as a bar chart using `matplotlib`.

## Requirements
- Python 3.x
- pandas
- matplotlib

## How to Run
1. Run `task7_sales_summary.py`
2. A bar chart image named `sales_chart.png` will be saved and displayed.

## Output
- Terminal will display a DataFrame of sales.
- Revenue by product will be shown as a bar chart.

## Sample SQL Query
```sql
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product;
