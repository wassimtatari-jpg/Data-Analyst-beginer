import pandas as pd

sales=pd.read_csv("sales use loc isin.csv",sep=";")

print(sales.head(5))

details=sales[sales['city'].isin(["Tangier"])]
print(details)
print(details.loc[:,['city']])

print(sales[sales['city'].isin(["Tangier","Rabat"])].loc[:,['city','department',"sales"]])

print(sales[sales['city'].isin(['Tangier','Casablanca','Marrakech'])].loc[:,["city",'store','sales']])

print(sales[sales['city'].isin(["Tangier","Rabat"])&sales['department'].isin(['Electronics','Food'])].loc[:,['city','department','sales']])

print(sales[sales['city'].isin(['Tangier','Casablanca'])&sales['department'].isin(['Food','Electronics'])&sales['store'].isin(['A',"B"])].loc[:,['city','department','sales','store']])

print(sales[~sales['store'].isin(["C"])&sales['city'].isin(["Tangier","Rabat"])&sales['department'].isin(['Food','Electronics'])].loc[:,['city','department','sales']])

print(sales[~sales["department"].isin(['Clothing'])&sales['city'].isin(["Casablanca",'Tangier'])&sales['store'].isin(["A","C"])].loc[:,['city','department','sales','store']])