import pandas as pd

# Load the CSV files
df1 = pd.read_csv("daily_sales_data_0.csv")
df2 = pd.read_csv("daily_sales_data_1.csv")
df3 = pd.read_csv("daily_sales_data_2.csv")

# Combine all data into one DataFrame
df = pd.concat([df1, df2, df3], ignore_index=True)

# Keep only Pink Morsel rows
df = df[df["product"] == "Pink Morsel"]

# Create Sales column
df["Sales"] = df["quantity"] * df["price"]

# Keep only required columns
final_df = df[["Sales", "date", "region"]]

# Save the final output
final_df.to_csv("pink_morsel_sales.csv", index=False)
