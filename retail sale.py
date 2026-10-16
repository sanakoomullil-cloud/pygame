import numpy as np
import pandas as pd

np.random.seed(42)
df = pd.DataFrame(
    {
        "Transaction_ID": range(101, 161),
        "Store": np.random.choice(
            ["Store A", "Store B", "Store C", "Store D"], 60
        ),
        "Category": np.random.choice(
            ["Electronics", "Clothing", "Home", "Books"], 60
        ),
        "Price": np.round(np.random.uniform(5.0, 150.0, 60), 2),
        "Quantity": np.random.randint(1, 10, 60),
    }
)

df["Total_Revenue"] = df["Price"] * df["Quantity"]
df["Order_Size"] = df["Total_Revenue"].apply(
    lambda r: (
        "High Value" if r > 500 else ("Medium Value" if r > 150 else "Low Value")
    )
)

filtered_df = df[df["Quantity"] > 2].sort_values(
    "Total_Revenue", ascending=False
)
store_perf = df.groupby("Store")["Total_Revenue"].sum().reset_index()

print(df.head())
print(store_perf.sort_values("Total_Revenue", ascending=False))
