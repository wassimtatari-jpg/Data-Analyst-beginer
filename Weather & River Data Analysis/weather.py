import pandas as pd
#read file csv
weather=pd.read_csv('weather_data.csv',sep=";")
#see the first 5 clum
print(weather.head(5))
print("="*30)
#count mean temprature using mean
mean_temprature=weather['temperature_c'].mean()
print("Mean Temprature")
print(mean_temprature)
print("="*30)
#count median of trmprature using median
median_temprature=weather["temperature_c"].median()
print("Median Temprature")
print(median_temprature)
print("="*30)
#most value repeat
most_temprature_repeat=weather["temperature_c"].mode()
print("Most temperture repeat")
print(most_temprature_repeat)
print("="*30)
#know min temprature
min_temprature=weather["temperature_c"].min()
print("Smaller Temprature ")
print(min_temprature)
print("="*30)
#know bigger temprature
max_temprature=weather["temperature_c"].max()
print("Higgest Temperature")
print(max_temprature)
print("="*30)
#use quantile
rain_fall_25=weather['rainfall_mm'].quantile(0.25)
print("25% of rain fall")
print(rain_fall_25)
rain_fall_75=weather['rainfall_mm'].quantile(0.75)
print("75% of rain fall")
print(rain_fall_75)
#using several method togather by agg
detail_temprature=weather["temperature_c"].agg(['mean','median',min,max])
print(detail_temprature)
print("="*20)
#count hight level by cummax
high_river=weather['river_level_cm'].cummax()
print(high_river)
sum_rain=weather["rainfall_mm"].cumsum()
print(sum_rain)