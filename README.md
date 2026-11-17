# Customer Sales Performance & Business Analytics Dashboard

## Project Overview

This project analyzes Brazilian e-commerce sales data to understand
revenue performance, customer behavior, product performance, and
regional sales. It uses Python, Pandas, Matplotlib, and Seaborn to
integrate datasets, prepare business metrics, generate visualizations,
and export reports.

## Objectives

-   Integrate customer, order, order-item, and product datasets.
-   Clean and transform business data.
-   Engineer revenue and time-based features.
-   Calculate key business performance indicators (KPIs).
-   Analyze monthly revenue, customers, products, and states.
-   Segment customers by revenue.
-   Produce charts and business reports.

## Tools and Libraries

Python 3.12, Pandas, Matplotlib, Seaborn, OpenPyXL, ReportLab, and
Visual Studio Code.

## Dataset

The project uses the Olist Brazilian e-commerce dataset. The main source
files are `olist_orders_dataset.csv`, `olist_order_items_dataset.csv`,
`olist_customers_dataset.csv`, and `olist_products_dataset.csv`. Place
them inside the `dataset` folder.

## Key Results

-   Total revenue (product price, excluding freight): **13,591,643.70
    BRL**
-   Unique orders: **98,666**
-   Unique customers: **95,420**
-   Unique products: **32,951**
-   Items sold: **112,650**
-   Average order value: **137.75 BRL**

Revenue is calculated from the item `price` field. Freight is excluded
from the revenue KPI. Profit is not calculated because product cost data
is not available.

## Analysis and Visualizations

-   Monthly revenue trend
-   Monthly revenue heatmap
-   Top 10 customers by revenue
-   Top 10 products by revenue
-   Revenue by customer state
-   Revenue by customer segment
-   KPI calculations and integrated sales dataset

September 2018 contains only one sales record in this dataset extract.
Its low revenue should not be interpreted as a confirmed business
decline.

## Reports and Outputs

The project includes or generates an integrated sales CSV, business KPI
report, dashboard image, business charts, Excel business analytics
report, and PDF business report. Include the output files that are
present in your final project folder.

## How to Run

1.  Install Python 3.12.
2.  Install libraries:
    `pip install pandas matplotlib seaborn openpyxl reportlab`
3.  Open the project folder in Visual Studio Code.
4.  Ensure the source CSV files are inside the `dataset` folder.
5.  From the project root, run: `py -3.12 dataset/day13_mini_project.py`

## Project Structure

``` text
customer_sales_analytics/
├── dataset/
│   ├── olist_orders_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_customers_dataset.csv
│   ├── olist_products_dataset.csv
│   └── day13_mini_project.py
├── day13_integrated_sales_data.csv
├── final_customer_sales_dashboard.png
├── day12_customer_sales_report.pdf
├── day11_business_analytics_report.xlsx
└── README.md
```

The exact output files depend on which scripts have been run.

## Conclusion

This project demonstrates a Python-based business analytics workflow,
from multi-dataset integration and feature engineering to KPI
calculation, customer and product analysis, visualization, and report
generation. The findings help describe sales patterns and identify
high-revenue customers, products, and regions.
