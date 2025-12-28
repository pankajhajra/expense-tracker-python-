import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

st.title("📊 Expense Analyzer Project (Hosted Version)")

# Step 1: Create CSV if not exists
file_name = "expenses.csv"

if not os.path.exists(file_name):
    sample_data = {
        "Date": ["2025-01-01","2025-01-01","2025-01-02","2025-01-03","2025-01-03"],
        "Category": ["Food","Travel","Food","Shopping","Rent"],
        "Amount": [120, 50, 150, 300, 5000]
    }
    df = pd.DataFrame(sample_data)
    df.to_csv(file_name, index=False)
    st.success("📁 expenses.csv file created automatically!")

#  Load data
data = pd.read_csv(file_name)

#  Data Cleaning
data["Amount"] = pd.to_numeric(data["Amount"], errors="coerce")
data = data.dropna()

st.write("### 📄 Expense Data Preview:")
st.dataframe(data)

#  Expense Analysis
st.write("### 💰 Total Expense:", np.sum(data["Amount"]))
st.write("### 📌 Average Expense:", np.mean(data["Amount"]))

category_expense = data.groupby("Category")["Amount"].sum()

st.write("### 📊 Category-wise Summary:")
st.bar_chart(category_expense)
