import pandas as pd

sales = pd.DataFrame({
    "store": [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],
    "type": ["A", "A", "A", "B", "B", "B",
             "A", "A", "A", "B", "B", "B"],
    "department": [1, 2, 3, 1, 2, 3,
                   1, 2, 3, 1, 2, 3],
    "weekly_sales": [15000, 22000, 18000,
                     12000, 25000, 20000,
                     17000, 24000, 16000,
                     14000, 28000, 21000]
})
#count by group
count_store_slaes=sales.groupby("type")["weekly_sales"].sum()
print("Total  Weekly sales by type")
print("-"*25)
print(count_store_slaes)
print("-"*25)
#count by groub for several 
count_store_slaes2=sales.groupby(["type","department"])["weekly_sales"].sum()
print("Total  Weekly sales by type for every department")
print("-"*30)
print(count_store_slaes2)
print("-"*30)
#count by group and several opertion
count_store_slaes3=sales.groupby("type")['weekly_sales'].agg([min,max,"mean","median"])
print(count_store_slaes3)
print("-"*30)
#count more operation
count_store_slaes4=sales.groupby(['type','department'])['weekly_sales'].agg(["mean",max,sum])
print(count_store_slaes4)
print("-"*30)
department=sales.loc[sales['department'].isin([1,3])]
count_store_slaes5=department.groupby('type')['weekly_sales'].agg(["mean",sum,"count"])
print(count_store_slaes5)