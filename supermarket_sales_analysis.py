# ============================================
# Supermarket Sales Analysis
# Beginner Data Analysis Project
# Tools: pandas, matplotlib, seaborn
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── 1. LOAD THE DATA ────────────────────────
df = pd.read_csv("supermarket_sales.csv")

# ── 2. EXPLORE THE DATA ─────────────────────
print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)
print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns\n")
print("First 5 rows:")
print(df.head())
print("\nColumn names:", df.columns.tolist())
print("\nBasic statistics:")
print(df.describe())

# ── 3. DATA CLEANING ────────────────────────
# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Extract month name from Date
df["Month"] = df["Date"].dt.month_name()

# Extract hour from Time column
df["Hour"] = pd.to_datetime(df["Time"], format="%H:%M").dt.hour

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# ── 4. ANALYSIS & VISUALIZATION ─────────────

# Set a clean style for all charts
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Supermarket Sales Analysis", fontsize=16, fontweight="bold")

# --- Chart 1: Sales by Product Line ---
product_sales = df.groupby("Product line")["Total"].sum().sort_values(ascending=False)
axes[0, 0].bar(product_sales.index, product_sales.values, color="steelblue")
axes[0, 0].set_title("Total Sales by Product Category")
axes[0, 0].set_xlabel("Product Category")
axes[0, 0].set_ylabel("Total Sales ($)")
axes[0, 0].tick_params(axis="x", rotation=30)

# --- Chart 2: Sales by City ---
city_sales = df.groupby("City")["Total"].sum()
axes[0, 1].pie(city_sales.values, labels=city_sales.index, autopct="%1.1f%%",
               colors=["#4C72B0", "#55A868", "#C44E52"])
axes[0, 1].set_title("Revenue Share by City")

# --- Chart 3: Customer Count by Hour ---
hourly = df["Hour"].value_counts().sort_index()
axes[1, 0].plot(hourly.index, hourly.values, marker="o", color="darkorange", linewidth=2)
axes[1, 0].set_title("Customer Visits by Hour of Day")
axes[1, 0].set_xlabel("Hour (24h)")
axes[1, 0].set_ylabel("Number of Transactions")
axes[1, 0].set_xticks(hourly.index)

# --- Chart 4: Average Rating by Branch ---
branch_rating = df.groupby("Branch")["Rating"].mean().sort_values(ascending=False)
bars = axes[1, 1].bar(branch_rating.index, branch_rating.values, color=["#4C72B0", "#55A868", "#C44E52"])
axes[1, 1].set_title("Average Customer Rating by Branch")
axes[1, 1].set_xlabel("Branch")
axes[1, 1].set_ylabel("Average Rating (out of 10)")
axes[1, 1].set_ylim(0, 10)
for bar, val in zip(bars, branch_rating.values):
    axes[1, 1].text(bar.get_x() + bar.get_width() / 2, val + 0.1,
                    f"{val:.2f}", ha="center", fontsize=11)

plt.tight_layout()
plt.savefig("sales_analysis.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nChart saved as sales_analysis.png")

# ── 5. SUMMARY STATISTICS ───────────────────
print("\n" + "=" * 50)
print("KEY INSIGHTS")
print("=" * 50)
print(f"Total Revenue:         ${df['Total'].sum():,.2f}")
print(f"Average Transaction:   ${df['Total'].mean():,.2f}")
print(f"Best Product Category: {product_sales.idxmax()}")
print(f"Top City by Revenue:   {city_sales.idxmax()}")
print(f"Peak Shopping Hour:    {hourly.idxmax()}:00")
print(f"Highest Rated Branch:  Branch {branch_rating.idxmax()}")
print(f"Most Used Payment:     {df['Payment'].value_counts().idxmax()}")
