#import and read file
import pandas as pd

weather=pd.read_csv("weather and method.csv",sep=";")
weather['date']=pd.to_datetime(weather["date"])
print(weather.head(3))
print(weather.info())
#slice using iloc
print(weather.iloc[5:12])

#slice using loc

print(weather.loc[5:12])

#slice using loc index and col

print(weather.loc[5:12,"avg_temp_c":"humidity_pct"])

#slice using loc index and col
print(weather.loc[12:20,"date":"max_temp_c"])
print(weather.loc[8:18,"city":])
print(weather.loc[:15,:"max_temp_c"])

date_sort=weather.set_index("date").sort_index()
print(date_sort)
print(date_sort.loc['2010-8':"2011-2"])