import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Laptop", "Mouse", None],
    "Quantity": [5, None, 8, 3, 2, None, 4],
    "Price": [800, 20, 50, 200, None, 20, 50]
}

df = pd.DataFrame(data)
df.fillna(df.mean(numeric_only = True), inplace=True)


print("The missing data with value: ", df)