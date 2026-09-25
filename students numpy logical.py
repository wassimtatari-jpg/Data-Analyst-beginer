import pandas as pd

students = pd.DataFrame({
    "name": ["Ali", "Sara", "Omar", "Lina", "Youssef", "Maya"],
    "age": [17, 22, 19, 25, 21, 30],
    "score": [65, 88, 72, 95, 81, 60]
})

import numpy as np

age_students=students['age']
score_students=students["score"]
between=np.logical_and(age_students>=18,age_students<=25)
between=np.logical_and(between,score_students>=75)
selected=students[between]
print(selected)