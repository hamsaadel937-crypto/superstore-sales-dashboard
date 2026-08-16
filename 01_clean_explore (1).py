"""
Superstore Data Analysis Project
Step 1: Cleaning + Exploratory Data Analysis (EDA)
"""
import pandas as pd

# --------------------------------------------------
# 1) تحميل البيانات
# --------------------------------------------------
df = pd.read_csv("superstore_raw.csv", encoding="utf-8")
print("=" * 60)
print("Shape (rows, columns):", df.shape)
print("=" * 60)
print(df.info())

# --------------------------------------------------
# 2) فحص القيم الفاضية
# --------------------------------------------------
print("\n" + "=" * 60)
print("Missing values per column:")
print(df.isnull().sum())

# --------------------------------------------------
# 3) فحص التكرار
# --------------------------------------------------
print("\n" + "=" * 60)
print("Duplicate rows:", df.duplicated().sum())

# --------------------------------------------------
# 4) تنظيف فعلي: شيل الصفوف الفاضية بالكامل وشيل التكرار
# --------------------------------------------------
rows_before = len(df)
# الصفوف اللي أعمدتها الأساسية (Sales/Order Date/Category) فاضية = صفوف تالفة، مش مفيدة للتحليل
essential_cols = ["Order Date", "Sales", "Category", "Region"]
df = df.dropna(subset=essential_cols)
df = df.drop_duplicates()
rows_after = len(df)
print(f"\nتم حذف {rows_before - rows_after} صف (بيانات تالفة / مكررة). الصفوف المتبقية: {rows_after}")

# --------------------------------------------------
# 5) تصحيح أنواع الأعمدة
# --------------------------------------------------
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")

# مدة الشحن (يوم)
df["Shipping Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

# أعمدة زمنية مفيدة للداشبورد
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Order Month Name"] = df["Order Date"].dt.strftime("%b")

# --------------------------------------------------
# 6) شيل الأعمدة الغير محتاجينها (Row ID مكرر مع الـ index)
# --------------------------------------------------
df = df.drop(columns=["Row ID"])

# --------------------------------------------------
# 7) حفظ نسخة نضيفة جاهزة لـ Power BI
# --------------------------------------------------
df.to_csv("superstore_clean.csv", index=False, encoding="utf-8-sig")
print("\n" + "=" * 60)
print("تم حفظ الملف النضيف: superstore_clean.csv")
print("Shape بعد التنظيف:", df.shape)

# --------------------------------------------------
# 8) استكشاف أولي (EDA) - أسئلة تحليلية أساسية
# --------------------------------------------------
print("\n" + "=" * 60)
print("EDA - إجابات أسئلة تحليلية أساسية")
print("=" * 60)

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
profit_margin = (total_profit / total_sales) * 100

print(f"\nإجمالي المبيعات: ${total_sales:,.2f}")
print(f"إجمالي الأرباح: ${total_profit:,.2f}")
print(f"هامش الربح العام: {profit_margin:.2f}%")

print("\n--- المبيعات والأرباح حسب الفئة ---")
by_category = df.groupby("Category")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False)
print(by_category)

print("\n--- أكتر 5 فئات فرعية خسارة (لو موجودة) ---")
by_subcat = df.groupby("Sub-Category")["Profit"].sum().sort_values()
print(by_subcat.head(5))

print("\n--- المبيعات حسب المنطقة ---")
by_region = df.groupby("Region")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False)
print(by_region)

print("\n--- تأثير الخصم على الربح (متوسط الربح حسب مستوى الخصم) ---")
df["Discount Band"] = pd.cut(df["Discount"], bins=[-0.01, 0, 0.2, 0.4, 1], labels=["0%", "0-20%", "20-40%", "40%+"])
print(df.groupby("Discount Band", observed=True)["Profit"].mean())

print("\n--- أكتر 10 منتجات مبيعًا (بالقيمة) ---")
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
print(top_products)

print("\n--- المبيعات الشهرية على مستوى السنوات ---")
monthly = df.groupby(["Order Year", "Order Month"])["Sales"].sum()
print(monthly)
