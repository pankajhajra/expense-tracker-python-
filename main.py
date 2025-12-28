# Expense Analyzer Project
# Using NumPy, Pandas, Matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os




file_name = "expenses.csv"

if not os.path.exists(file_name):
    sample_data = {
        "Date": [
            "2025-01-01", "2025-01-01",
            "2025-01-02", "2025-01-03",
            "2025-01-03"
        ],
        "Category": [
            "Food", "Travel",
            "Food", "Shopping",
            "Rent"
        ],
        "Amount": [
            120, 50,
            150, 300,
            5000
        ]
    }

    df = pd.DataFrame(sample_data)
    df.to_csv(file_name, index=False)
    print("expenses.csv file created successfully\n")

#  Load data

data = pd.read_csv(file_name)

 
#  Data cleaning
 
data["Amount"] = pd.to_numeric(data["Amount"], errors="coerce")
data = data.dropna()

 
# Step 4: Analysis

# Total expense
total_expense = np.sum(data["Amount"])
print("Total Expense:", total_expense)

# Category-wise expense
category_expense = data.groupby("Category")["Amount"].sum()
print("\nCategory-wise Expense:")
print(category_expense)

# Average expense
avg_expense = np.mean(data["Amount"])
print("\nAverage Expense:", avg_expense)

#  Visualization by using  matplotlib.
plt.figure()
category_expense.plot(kind="bar", title="Category-wise Expenses")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()
