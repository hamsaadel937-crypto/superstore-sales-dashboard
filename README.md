# 📊 Superstore Sales & Profitability Analysis

An end-to-end **Data Analytics project** using Python, Pandas, Power BI, and DAX to analyze sales performance, profitability, discounts, products, and regional trends.

---

## 🎯 Project Overview

The goal of this project is to analyze the Superstore dataset and answer key business questions such as:

- How are sales and profit performing?
- Which categories and sub-categories are most and least profitable?
- How do discounts affect profitability?
- Which regions generate the highest sales and profit?
- Which products contribute most to the business?
- Which months show the strongest sales performance?

The analysis combines **Python-based data preparation and exploration** with an interactive **Power BI dashboard**.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| 🐍 Python | Data cleaning & exploration |
| 🐼 Pandas | Data manipulation |
| 📊 Power BI | Interactive dashboard |
| 🧮 DAX | Measures & calculations |
| 📁 CSV | Dataset storage |

---

## 🔄 Project Workflow

```text
Raw Data
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Business Analysis
   ↓
Power BI Dashboard
   ↓
Insights & Recommendations
🧹 Data Preparation

The dataset was cleaned and prepared using Python and Pandas.

Main preprocessing steps included:

Checking missing values
Checking duplicate records
Validating data types
Cleaning inconsistent values
Preparing the dataset for Power BI
Exporting the cleaned dataset
Dataset Files
superstore_raw.csv → Original dataset
superstore_clean.csv → Cleaned dataset
📈 Key Analysis Areas
💰 Sales & Profitability

Analyzed:

Total Sales
Total Profit
Profit Margin
Sales by Category
Profit by Category
Sales by Region
🏷️ Discount Analysis

Investigated the relationship between discount levels and profitability.

The analysis shows that higher discount levels are strongly associated with lower profitability, with heavy discounts potentially turning profitable transactions into losses.

📦 Product Analysis

Identified:

Most profitable products
Least profitable products
High-sales but low-profit products
Loss-making sub-categories
🌍 Regional Analysis

Compared sales and profitability across different regions to identify the strongest and weakest performing markets.

📅 Time Analysis

Analyzed monthly and yearly sales trends to identify periods of stronger business performance.

💡 Key Insights

Based on the analysis:

📊 Overall Profit Margin is approximately 12.47%.
🏷️ High discount levels are associated with significantly lower profit.
📦 Some sub-categories generate high sales but weak or negative profitability.
🌎 The West region shows strong sales performance.
📅 November and December are among the strongest months in terms of sales.
💰 Sales volume alone does not always indicate profitability.
🎯 Business Recommendations

Based on the findings, the business could:

Review high-discount transactions
Reduce excessive discounting, especially where margins are already low.
Optimize product pricing
Review pricing strategies for products and sub-categories with weak profitability.
Focus on profitable products
Increase attention and marketing efforts toward products with strong profit margins.
Investigate loss-making categories
Identify the reasons behind negative profitability and evaluate whether pricing, discounts, or costs should be adjusted.
Prepare for peak sales periods
Improve inventory and marketing planning ahead of high-performing months such as November and December.
📊 Power BI Dashboard

The Power BI dashboard provides an interactive view of:

Sales Performance
Profitability
Regional Performance
Category & Sub-Category Analysis
Discount & Profitability Relationship
Product Performance
Time Trends

📌 The dashboard is designed to help decision-makers quickly identify sales and profitability patterns.

📁 Repository Structure
superstore-sales-dashboard/
│
├── 01_clean_explore.py
├── superstore_raw.csv
├── superstore_clean.csv
├── README.md
│
└── screenshots/
    ├── dashboard_overview.png
    ├── product_analysis.png
    └── discount_analysis.png
🚀 Future Improvements

Possible future improvements include:

Adding more advanced DAX measures
Creating additional Power BI pages
Adding customer segmentation
Building sales forecasting
Adding interactive drill-through analysis
Automating the data cleaning pipeline
👩‍💻 Author

Hamsa Adel

AI & Data Science Student
Interested in Data Analysis, Business Intelligence, Python, SQL, and Power BI.
