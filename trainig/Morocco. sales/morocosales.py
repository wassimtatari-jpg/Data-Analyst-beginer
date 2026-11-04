import pandas as pd

morocco_sales=pd.read_csv('moroco sales.csv',sep=";")

morocco_sales_table=morocco_sales.pivot_table(values="sales",index="store",columns="department",aggfunc=sum,fill_value=0,margins=True)

print(morocco_sales_table)