# Supermarket Sales Analysis

A beginner-level data analysis project using Python, pandas, and Matplotlib to explore supermarket sales data.

## Project Overview

This project analyzes a supermarket sales dataset to find useful insights such as:
- Which product category has the highest sales
- Which city generates the most revenue
- What time of day has the most customers
- Sales trends across months

## Tools & Libraries Used

- Python 3
- pandas
- matplotlib
- seaborn
- Jupyter Notebook

## Dataset

The dataset contains supermarket sales records with columns like:
- Branch (A, B, C)
- City
- Customer type
- Product line
- Unit price, Quantity, Total
- Date and Time
- Payment method
- Rating

Source: [Kaggle - Supermarket Sales Dataset](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales)

## Project Structure

```
supermarket-sales-analysis/
├── README.md
├── supermarket_sales_analysis.py   # Main Python script
├── analysis_notebook.ipynb         # Jupyter Notebook version
└── supermarket_sales.csv           # Dataset (download from Kaggle link above)
```

## How to Run

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/python-data-analysis.git
```

2. Install required libraries:
```bash
pip install pandas matplotlib seaborn
```

3. Download the dataset from Kaggle and place `supermarket_sales.csv` in the project folder.

4. Run the script:
```bash
python supermarket_sales_analysis.py
```

## Key Insights Found

- Branch C had the highest average customer rating
- Food & Beverages was the top-selling product category
- Most purchases happened between 7 PM and 9 PM
- Female customers slightly outnumbered male customers

## What I Learned

- Loading and exploring data with pandas
- Cleaning and filtering DataFrames
- Creating bar charts, pie charts, and histograms with matplotlib
- Finding patterns in real-world data

---
*This is a beginner project created while learning data analysis with Python.*
