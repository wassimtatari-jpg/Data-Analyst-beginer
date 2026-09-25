import pandas as pd

cars = pd.DataFrame({
    "brand": ["Dacia", "Hyundai", "Toyota", "Volkswagen", "BYD", "Kia"],
    "cars_per_cap": [80, 150, 320, 550, 420, 700]
})

import numpy as np
car=cars["cars_per_cap"]
between=np.logical_and(car>150,car<500)
selected=cars[between]
print(selected)

