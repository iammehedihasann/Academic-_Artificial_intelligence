import pandas as pd

# Load the CSV file (Ensure the correct file extension is used)
df = pd.read_csv("E:/2025_January/CSV_File_for_Task.csv")

# Ensure column names match your CSV file
df["Revenue"] = df["Product Quality"] * df["Price"]

# Compute total revenue per product
total_revenue = df.groupby("Product")["Revenue"].sum().reset_index()

# Display the result
print(total_revenue)
