import pandas as pd

weather=pd.read_csv("weather.csv",sep=';')

print(weather.head(5))
weather.info()
print(weather.describe())
print(weather.shape)
print(weather.values)
print(weather.columns)
print(weather.index)