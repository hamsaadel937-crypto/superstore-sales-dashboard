"""
Superstore Sales & Profitability Analysis
Step 1: Data Cleaning + Exploratory Data Analysis (EDA)
Step 2: Statistical Analysis + Business Insights
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ==================================================
# 1) LOAD DATA
# ==================================================

df = pd.read_csv("superstore_raw.csv", encoding="utf-8")

print("=" * 70)
print("SUPERSTORE SALES & PROFITABILITY ANALYSIS")
print("=" * 70)

print("\nDataset Shape:", df.shape)

print("\nDataset Information:")
print(df.info())


# ==================================================
# 2) DATA QUALITY CHECK
# ==================================================

print("\n" + "=" * 70)
print("MISSING VALUES")
print("=" * 70)

missing_values = df.isnull().sum()

print(missing_values)

print("\nTotal Missing Values:", missing_values.sum())


print("\n" + "=" * 70)
print("DUPLICATE RECORDS")
print("=" * 70)

duplicates = df.duplicated().sum()

print("Duplicate rows:", duplicates)


# ==================================================
# 3) DATA CLEANING
# ==================================================

print("\n" + "=" * 70)
print("DATA CLEANING")
print("=" * 70)

rows_before = len(df)

# Important columns required for analysis
essential_cols = [
    "Order Date",
    "Sales",
    "Category",
    "Region"
]

# Remove rows with missing essential information
df = df.dropna(subset=essential_cols)

# Remove duplicate records
df = df.drop_duplicates()

rows_after = len(df)

print("Rows before cleaning:", rows_before)
print("Rows after cleaning:", rows_after)
print("Rows removed:", rows_before - rows_after)


# ==================================================
# 4) DATA TYPES
# ==================================================

print("\n" + "=" * 70)
print("DATA TYPE CONVERSION")
print("=" * 70)

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="%m/%d/%Y"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    format="%m/%d/%Y"
)

print("Order Date converted to datetime.")
print("Ship Date converted to datetime.")


# ==================================================
# 5) FEATURE ENGINEERING
# ==================================================

print("\n" + "=" * 70)
print("FEATURE ENGINEERING")
print("=" * 70)

# Shipping duration
df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

# Time features
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Order Month Name"] = df["Order Date"].dt.strftime("%b")

# Discount categories
df["Discount Band"] = pd.cut(
    df["Discount"],
    bins=[-0.01, 0, 0.2, 0.4, 1],
    labels=[
        "0%",
        "0-20%",
        "20-40%",
        "40%+"
    ]
)

print("Created:")
print("- Shipping Days")
print("- Order Year")
print("- Order Month")
print("- Order Month Name")
print("- Discount Band")


# ==================================================
# 6) REMOVE UNNECESSARY COLUMNS
# ==================================================

if "Row ID" in df.columns:
    df = df.drop(columns=["Row ID"])

print("\nUnnecessary identifier columns removed.")


# ==================================================
# 7) DESCRIPTIVE STATISTICS
# ==================================================

print("\n" + "=" * 70)
print("DESCRIPTIVE STATISTICS")
print("=" * 70)

numeric_columns = [
    "Sales",
    "Quantity",
    "Discount",
    "Profit",
    "Shipping Days"
]

statistics = df[numeric_columns].describe().T

statistics["median"] = df[numeric_columns].median()

print(statistics)


# ==================================================
# 8) SALES & PROFITABILITY ANALYSIS
# ==================================================

print("\n" + "=" * 70)
print("SALES & PROFITABILITY")
print("=" * 70)

total_sales = df["Sales"].sum()

total_profit = df["Profit"].sum()

profit_margin = (
    total_profit / total_sales
) * 100

average_sales = df["Sales"].mean()

average_profit = df["Profit"].mean()

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")
print(f"Average Sales per Record: ${average_sales:,.2f}")
print(f"Average Profit per Record: ${average_profit:,.2f}")


# ==================================================
# 9) CATEGORY ANALYSIS
# ==================================================

print("\n" + "=" * 70)
print("CATEGORY ANALYSIS")
print("=" * 70)

category_analysis = (
    df.groupby("Category")[["Sales", "Profit"]]
    .sum()
    .sort_values("Sales", ascending=False)
)

category_analysis["Profit Margin %"] = (
    category_analysis["Profit"]
    / category_analysis["Sales"]
) * 100

print(category_analysis)


# ==================================================
# 10) SUB-CATEGORY PROFITABILITY
# ==================================================

print("\n" + "=" * 70)
print("SUB-CATEGORY PROFITABILITY")
print("=" * 70)

sub_category_analysis = (
    df.groupby("Sub-Category")[["Sales", "Profit"]]
    .sum()
    .sort_values("Profit")
)

print("\nLowest Profit Sub-Categories:")
print(sub_category_analysis.head(5))

print("\nHighest Profit Sub-Categories:")
print(sub_category_analysis.tail(5))


# ==================================================
# 11) REGIONAL ANALYSIS
# ==================================================

print("\n" + "=" * 70)
print("REGIONAL ANALYSIS")
print("=" * 70)

region_analysis = (
    df.groupby("Region")[["Sales", "Profit"]]
    .sum()
    .sort_values("Sales", ascending=False)
)

region_analysis["Profit Margin %"] = (
    region_analysis["Profit"]
    / region_analysis["Sales"]
) * 100

print(region_analysis)


# ==================================================
# 12) DISCOUNT ANALYSIS
# ==================================================

print("\n" + "=" * 70)
print("DISCOUNT & PROFITABILITY ANALYSIS")
print("=" * 70)

discount_analysis = (
    df.groupby("Discount Band", observed=True)
    .agg(
        Average_Discount=("Discount", "mean"),
        Average_Profit=("Profit", "mean"),
        Total_Profit=("Profit", "sum"),
        Sales=("Sales", "sum")
    )
)

print(discount_analysis)


# ==================================================
# 13) DISCOUNT VS PROFIT CORRELATION
# ==================================================

print("\n" + "=" * 70)
print("DISCOUNT VS PROFIT CORRELATION")
print("=" * 70)

discount_profit_corr = df[
    ["Discount", "Profit"]
].corr().loc["Discount", "Profit"]

print(
    f"Correlation between Discount and Profit: "
    f"{discount_profit_corr:.4f}"
)

if discount_profit_corr < 0:
    print(
        "Insight: Higher discounts are associated "
        "with lower profitability."
    )
else:
    print(
        "Insight: The relationship between discount "
        "and profit is not negative."
    )


# ==================================================
# 14) PRODUCT ANALYSIS
# ==================================================

print("\n" + "=" * 70)
print("PRODUCT ANALYSIS")
print("=" * 70)

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Sales:")
print(top_products)


top_profit_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Profit:")
print(top_profit_products)


loss_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values()
    .head(10)
)

print("\nTop 10 Loss-Making Products:")
print(loss_products)


# ==================================================
# 15) CUSTOMER ANALYSIS
# ==================================================

print("\n" + "=" * 70)
print("CUSTOMER ANALYSIS")
print("=" * 70)

customer_analysis = (
    df.groupby("Customer Name")[["Sales", "Profit"]]
    .sum()
    .sort_values("Sales", ascending=False)
)

print("\nTop 10 Customers by Sales:")
print(customer_analysis.head(10))


print("\nTop 10 Customers by Profit:")

top_customer_profit = (
    customer_analysis
    .sort_values("Profit", ascending=False)
    .head(10)
)

print(top_customer_profit)


# ==================================================
# 16) SHIPPING ANALYSIS
# ==================================================

print("\n" + "=" * 70)
print("SHIPPING ANALYSIS")
print("=" * 70)

average_shipping_days = df["Shipping Days"].mean()

median_shipping_days = df["Shipping Days"].median()

print(
    f"Average Shipping Days: "
    f"{average_shipping_days:.2f}"
)

print(
    f"Median Shipping Days: "
    f"{median_shipping_days:.2f}"
)


shipping_summary = (
    df.groupby("Ship Mode")["Shipping Days"]
    .mean()
    .sort_values()
)

print("\nAverage Shipping Days by Ship Mode:")
print(shipping_summary)


# ==================================================
# 17) MONTHLY SALES ANALYSIS
# ==================================================

print("\n" + "=" * 70)
print("MONTHLY SALES ANALYSIS")
print("=" * 70)

monthly_sales = (
    df.groupby(
        ["Order Year", "Order Month"]
    )["Sales"]
    .sum()
)

print(monthly_sales)


# Best sales month
monthly_summary = (
    df.groupby("Order Month")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop Sales Months:")
print(monthly_summary.head())


# ==================================================
# 18) OUTLIER DETECTION USING IQR
# ==================================================

print("\n" + "=" * 70)
print("OUTLIER DETECTION")
print("=" * 70)

Q1 = df["Sales"].quantile(0.25)

Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR

upper_bound = Q3 + 1.5 * IQR

sales_outliers = df[
    (df["Sales"] < lower_bound)
    | (df["Sales"] > upper_bound)
]

print(f"Q1: ${Q1:,.2f}")
print(f"Q3: ${Q3:,.2f}")
print(f"IQR: ${IQR:,.2f}")
print(f"Lower Bound: ${lower_bound:,.2f}")
print(f"Upper Bound: ${upper_bound:,.2f}")
print(
    "Number of Sales Outliers:",
    len(sales_outliers)
)


# ==================================================
# 19) PROFIT DISTRIBUTION
# ==================================================

print("\n" + "=" * 70)
print("PROFIT DISTRIBUTION")
print("=" * 70)

profit_mean = df["Profit"].mean()

profit_median = df["Profit"].median()

profit_std = df["Profit"].std()

print(f"Mean Profit: ${profit_mean:,.2f}")
print(f"Median Profit: ${profit_median:,.2f}")
print(f"Standard Deviation: ${profit_std:,.2f}")


# ==================================================
# 20) BUSINESS INSIGHTS
# ==================================================

print("\n" + "=" * 70)
print("KEY BUSINESS INSIGHTS")
print("=" * 70)

# Most profitable category
most_profitable_category = (
    category_analysis["Profit"]
    .idxmax()
)

# Least profitable category
least_profitable_category = (
    category_analysis["Profit"]
    .idxmin()
)

# Best region
best_region = (
    region_analysis["Sales"]
    .idxmax()
)

# Worst sub-category
worst_subcategory = (
    sub_category_analysis["Profit"]
    .idxmin()
)

print(
    f"\n1. Most profitable category: "
    f"{most_profitable_category}"
)

print(
    f"2. Least profitable category: "
    f"{least_profitable_category}"
)

print(
    f"3. Highest-sales region: "
    f"{best_region}"
)

print(
    f"4. Lowest-profit sub-category: "
    f"{worst_subcategory}"
)

print(
    f"5. Overall profit margin: "
    f"{profit_margin:.2f}%"
)

print(
    f"6. Discount-Profit correlation: "
    f"{discount_profit_corr:.4f}"
)


# ==================================================
# 21) VISUALIZATIONS
# ==================================================

print("\n" + "=" * 70)
print("GENERATING VISUALIZATIONS")
print("=" * 70)


# Sales by Category
category_analysis["Sales"].plot(
    kind="bar",
    figsize=(8, 5),
    title="Sales by Category"
)

plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


# Profit by Region
region_analysis["Profit"].plot(
    kind="bar",
    figsize=(8, 5),
    title="Profit by Region"
)

plt.xlabel("Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()


# Discount vs Profit
plt.figure(figsize=(8, 5))

plt.scatter(
    df["Discount"],
    df["Profit"],
    alpha=0.5
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()


# Profit Distribution
plt.figure(figsize=(8, 5))

plt.hist(
    df["Profit"],
    bins=30
)

plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


# ==================================================
# 22) SAVE CLEAN DATASET
# ==================================================

df.to_csv(
    "superstore_clean.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\n" + "=" * 70)
print("CLEAN DATASET SAVED")
print("=" * 70)

print("File: superstore_clean.csv")
print("Final Shape:", df.shape)

print("\nAnalysis completed successfully! 🚀")
