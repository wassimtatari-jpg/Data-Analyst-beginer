import pandas as pd

data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
    'Price': [800, None, 300, None],
    'Quantity': [5, 10, None, 7]
}

sales = pd.DataFrame(data)
#check if there is any value missing
print(sales.isna())
#Check if any value missing in Dataframe
print(sales.isna().any())
#Check if any value missing in the whole Dataframe
print(sales.isna().any().any())
#count how many value missing
print(sales.isna().sum())
#delete missing data
sales_complete=sales.dropna()
print(sales_complete)
#fill missing value
sales_filled=sales.fillna(0)
print(sales_filled)
print(sales_filled.isna().any().any())
import matplotlib.pyplot as plt

sales.isna().sum().plot(kind="bar")
plt.show()