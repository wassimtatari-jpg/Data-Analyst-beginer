import pandas as pd
sales=pd.read_csv('morocco sales2.csv',sep=";")
print(sales.head(3))
#using set index
transaction_id=sales.set_index("transaction_id")
print(transaction_id.head(3))
#sort index
new_sort=transaction_id.sort_index(ascending=False)
print(new_sort)
#use loc
print(transaction_id.loc[1012])
rest=transaction_id.reset_index()
print(rest)
#use isin 
cities=sales[sales["store"].isin(['Tangier','Casablanca'])]
print(cities)
#use isin  and loc
details=sales[sales['store'].isin(['Tangier','Casablanca'])&
               (sales["department"].isin(['Electronics','Furniture']))]
print(details.loc[:,['sales','department','store']])

details=sales.pivot_table(index="store",columns="department",values="sales",aggfunc=sum,fill_value=0,margins=True)
print(details)