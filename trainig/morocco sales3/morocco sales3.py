#import pandas and read file
import pandas as pd

sales=pd.read_csv("morocco sales3.csv",sep=";")
#show 5 row and show info
print(sales.head(5))
sales.info()
#Add cloum

sales['profit_mad']=sales['revenue_mad']-sales["cost_mad"]
print(sales.head(3))

#covert and add coulm
sales["date"]=pd.to_datetime(sales['date'],dayfirst=True)
sales['year']=sales['date'].dt.year
sales['month']=sales['date'].dt.month
sales['day']=sales['date'].dt.day
print(sales.head(3))
#use pivot table
details=sales.pivot_table(columns="city",values="revenue_mad",index="category",aggfunc=sum,fill_value=0,margins=True)
print(details)
#subset
sales_subset=sales.loc[:,["city",'category','product','revenue_mad',"profit_mad"]]
print(sales_subset)

print(sales.loc[sales['city'].isin(['Tangier']),["city","product","revenue_mad"]])


#MultiIndex creat

sales_index=sales.set_index(['city','category'])
print(sales_index.head(10))
#Chose Tangier and electronics
print(sales_index.loc[('Tangier','Electronics')])
#Chose only tangier and all categories
print(sales_index.loc["Tangier",:])
#chose two cities and all categories
print(sales_index.loc[(["Casablanca","Rabat"]),:])
#chose two cities and one category
print(sales_index.loc[(["Casablanca","Tangier"],['Electronics']),:])

#use mean and axis
mean_values=sales[['units_sold',"revenue_mad",'cost_mad','avg_temperature_c','profit_mad']].mean(axis=0,numeric_only=True)

print(mean_values)

#use mean and axis
mean_values=sales[['units_sold',"revenue_mad",'cost_mad','avg_temperature_c','profit_mad']].mean(axis=1,numeric_only=True)
print(mean_values)

#use idexmin

min_revenue_index=sales['revenue_mad'].idxmin()
print(min_revenue_index)
print(sales.loc[min_revenue_index])

min_revenue_index2=sales.groupby("city")['revenue_mad'].sum().idxmin()
print(min_revenue_index2)


print(sales.groupby("city")["revenue_mad"].sum().loc[min_revenue_index2])
#USE condtion
high_revenue=sales[sales['revenue_mad']>5000]
print(high_revenue)

high_revenue2=sales[(sales['revenue_mad']>5000)&(sales["city"]=="Tangier")]
print(high_revenue2)

city_revenue=sales[(sales['city']=="Tangier")|(sales['city']=="Rabat")]
print(city_revenue)

sales_without_tangier=sales[~(sales['city']=="Tangier")]
print(sales_without_tangier)

selected_cities=sales[sales['city'].isin(["Tangier","Casablanca",'Chefchaouen'])]

print(selected_cities)

selected_high_revenue=sales[(sales['city'].isin(["Tangier","Casablanca",'Chefchaouen']))&(sales['revenue_mad']>5000)]
print(selected_high_revenue)


print(sales[sales['revenue_mad'].between(3000,7000)])