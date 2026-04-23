import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

print("Dataset:\n", df)

# Total revenue
df["revenue"] = df["price"] * df["quantity"]
print("\nTotal Revenue:", df["revenue"].sum())

# Revenue by category
print("\nRevenue by Category:")
print(df.groupby("category")["revenue"].sum())

# Most sold product
print("\nMost Sold Product:")
print(df.groupby("product")["quantity"].sum().idxmax())

# Average price
print("\nAverage Price:", df["price"].mean())

# Top 3 highest revenue orders
print("\nTop Revenue Orders:")
print(df.sort_values(by="revenue", ascending=False).head(3))
