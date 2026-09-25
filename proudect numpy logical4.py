import pandas as pd

products = pd.DataFrame({
    "product": ["Laptop", "Phone", "Tablet", "Monitor", "Headphones", "Camera"],
    "price": [900, 600, 350, 450, 120, 800],
    "rating": [4.5, 4.2, 3.8, 4.7, 4.4, 3.9],
    "stock": [10, 25, 8, 15, 50, 5]
})
import numpy as np
selected_price=products['price']
selected_rating=products['rating']
selected_stock=products['stock']
between=np.logical_and(selected_price>=300,selected_price<=800)
between=np.logical_and(between,selected_rating>=4.0)
between=np.logical_and(between,selected_stock>10)
selected=products[between]
print(selected)