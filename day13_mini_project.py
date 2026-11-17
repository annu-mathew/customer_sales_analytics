import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
orders = pd.read_csv("dataset/olist_orders_dataset.csv")

order_items = pd.read_csv("dataset/olist_order_items_dataset.csv")

customers = pd.read_csv("dataset/olist_customers_dataset.csv")

products = pd.read_csv("dataset/olist_products_dataset.csv")

print("All datasets loaded successfully!")

print("Orders:", orders.shape)
print("Order Items:", order_items.shape)
print("Customers:", customers.shape)
print("Products:", products.shape)
sales_data = pd.merge(
    order_items,
    orders,
    on="order_id",
    how="inner",
    validate="many_to_one"
)

sales_data = pd.merge(
    sales_data,
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one"
)

sales_data = pd.merge(
    sales_data,
    products,
    on="product_id",
    how="left",
    validate="many_to_one"
)

print("All datasets merged successfully!")
print("Integrated Dataset Shape:", sales_data.shape)
print(sales_data.head())
sales_data["revenue"] = sales_data["price"]

sales_data["total_order_item_value"] = (
    sales_data["price"] + sales_data["freight_value"]
)

sales_data["order_purchase_timestamp"] = pd.to_datetime(
    sales_data["order_purchase_timestamp"],
    format="%d-%m-%Y %H:%M"
)

sales_data["year"] = sales_data["order_purchase_timestamp"].dt.year

sales_data["month"] = sales_data["order_purchase_timestamp"].dt.month

sales_data["month_name"] = sales_data["order_purchase_timestamp"].dt.month_name()

print("Business features created successfully!")

print(sales_data[[
    "price",
    "freight_value",
    "revenue",
    "total_order_item_value",
    "year",
    "month",
    "month_name"
]].head())
total_revenue = sales_data["revenue"].sum()

total_orders = sales_data["order_id"].nunique()

total_customers = sales_data["customer_unique_id"].nunique()

total_products = sales_data["product_id"].nunique()

total_items_sold = len(sales_data)

average_order_value = total_revenue / total_orders

print("\n===== BUSINESS KPI REPORT =====")

print("Total Revenue:", round(total_revenue, 2))

print("Total Orders:", total_orders)

print("Total Customers:", total_customers)

print("Total Products:", total_products)

print("Total Items Sold:", total_items_sold)

print("Average Order Value:", round(average_order_value, 2))
sales_data.to_csv(
    "day13_integrated_sales_data.csv",
    index=False
)

print("Integrated sales dataset saved successfully!")
monthly_sales = sales_data.groupby(
    ["year", "month", "month_name"]
)["revenue"].sum().reset_index()

monthly_sales = monthly_sales.sort_values(
    ["year", "month"]
)

print("\n===== MONTHLY SALES ANALYSIS =====")
print(monthly_sales.head(12))
plt.figure(figsize=(12, 6))

monthly_sales["period"] = (
    monthly_sales["year"].astype(str) + "-" +
    monthly_sales["month"].astype(str).str.zfill(2)
)

sns.lineplot(
    data=monthly_sales,
    x="period",
    y="revenue",
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Year-Month")
plt.ylabel("Revenue (BRL)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("day13_monthly_revenue_trend.png")
plt.show()
september_2018 = sales_data[
    (sales_data["year"] == 2018) &
    (sales_data["month"] == 9)
]

print("\n===== SEPTEMBER 2018 CHECK =====")
print("Number of sales records:", len(september_2018))
print("Total revenue:", september_2018["revenue"].sum())
print("Number of unique orders:", september_2018["order_id"].nunique())
revenue_pivot = monthly_sales.pivot(
    index="year",
    columns="month_name",
    values="revenue"
)

month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

revenue_pivot = revenue_pivot.reindex(columns=month_order)

plt.figure(figsize=(14, 6))

sns.heatmap(
    revenue_pivot,
    annot=True,
    fmt=".0f",
    cmap="YlGnBu"
)

plt.title("Monthly Revenue Heatmap")
plt.xlabel("Month")
plt.ylabel("Year")
plt.tight_layout()
plt.savefig("day13_revenue_heatmap.png")
plt.show()
customer_revenue = sales_data.groupby(
    "customer_unique_id"
)["revenue"].sum().reset_index()

top_10_customers = customer_revenue.sort_values(
    by="revenue",
    ascending=False
).head(10)

print("\n===== TOP 10 CUSTOMERS BY REVENUE =====")
print(top_10_customers)
plt.figure(figsize=(12, 6))

sns.barplot(
    data=top_10_customers,
    x="revenue",
    y="customer_unique_id"
)

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Revenue (BRL)")
plt.ylabel("Customer ID")
plt.tight_layout()
plt.savefig("day13_top10_customers.png")
plt.show()
product_revenue = sales_data.groupby(
    "product_id"
)["revenue"].sum().reset_index()

top_10_products = product_revenue.sort_values(
    by="revenue",
    ascending=False
).head(10)

print("\n===== TOP 10 PRODUCTS BY REVENUE =====")
print(top_10_products)
plt.figure(figsize=(12, 6))

sns.barplot(
    data=top_10_products,
    x="revenue",
    y="product_id"
)

plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue (BRL)")
plt.ylabel("Product ID")
plt.tight_layout()
plt.savefig("day13_top10_products.png")
plt.show()
state_revenue = sales_data.groupby(
    "customer_state"
)["revenue"].sum().reset_index()

state_revenue = state_revenue.sort_values(
    by="revenue",
    ascending=False
)

print("\n===== REVENUE BY STATE =====")
print(state_revenue.head(10))
plt.figure(figsize=(12, 6))

sns.barplot(
    data=state_revenue.head(10),
    x="revenue",
    y="customer_state"
)

plt.title("Top 10 States by Revenue")
plt.xlabel("Revenue (BRL)")
plt.ylabel("Customer State")
plt.tight_layout()
plt.savefig("day13_state_revenue.png")
plt.show()
customer_revenue["customer_segment"] = pd.qcut(
    customer_revenue["revenue"],
    q=3,
    labels=["Low", "Medium", "High"]
)

segment_summary = customer_revenue.groupby(
    "customer_segment",
    observed=True
)["revenue"].agg(
    ["count", "mean", "sum"]
).reset_index()

print("\n===== CUSTOMER SEGMENTATION =====")
print(segment_summary)
plt.figure(figsize=(10, 6))

sns.barplot(
    data=segment_summary,
    x="customer_segment",
    y="sum"
)

plt.title("Revenue by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Revenue (BRL)")
plt.tight_layout()
plt.savefig("day13_customer_segmentation.png")
plt.show()
kpi_summary = pd.DataFrame({
    "KPI": [
        "Total Revenue",
        "Total Orders",
        "Total Customers",
        "Total Products",
        "Total Items Sold",
        "Average Order Value"
    ],
    "Value": [
        total_revenue,
        total_orders,
        total_customers,
        total_products,
        total_items_sold,
        average_order_value
    ]
})

with pd.ExcelWriter("day13_mini_project_report.xlsx") as writer:
    kpi_summary.to_excel(writer, sheet_name="Business KPIs", index=False)
    monthly_sales.to_excel(writer, sheet_name="Monthly Revenue", index=False)
    top_10_customers.to_excel(writer, sheet_name="Top Customers", index=False)
    top_10_products.to_excel(writer, sheet_name="Top Products", index=False)
    state_revenue.to_excel(writer, sheet_name="State Revenue", index=False)
    segment_summary.to_excel(writer, sheet_name="Customer Segments", index=False)

print("Day 13 Excel report created successfully!")
df = pd.read_csv("day13_integrated_sales_data.csv")

sample_df = df.head(1000)

sample_df.to_csv("day13_integrated_sales_sample.csv", index=False)

print("Sample CSV created successfully!")