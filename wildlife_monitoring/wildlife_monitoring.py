import pandas as pd
import numpy as np
#read csv by panda and know info and describe
wildlife=pd.read_csv('wildlife_monitoring.csv',sep=';')
print(wildlife.info())
print(wildlife.describe())
print("="*60)
#discover repeted info
repeted_data=wildlife.duplicated(subset='animal')
print(wildlife.loc[repeted_data,'animal'])
#remove repeted data
wild_remove_repeted=wildlife.drop_duplicates(subset=['animal','region'])
print(wild_remove_repeted)
#counting
count_animal_conservation=wildlife['conservation_status'].value_counts()
print(count_animal_conservation)
print("="*30)
count_animal_conservation2=wildlife['conservation_status'].value_counts(sort=True)
print(count_animal_conservation2)
print("="*30)
count_animal_conservation3=wildlife['conservation_status'].value_counts(sort=False)
print(count_animal_conservation3)
print("="*30)
count_animal_conservation4=wildlife['conservation_status'].value_counts(normalize=True)
print(count_animal_conservation4)
print("="*30)
count_animal_conservation5=wildlife['conservation_status'].value_counts(normalize=True,sort=True)
print(count_animal_conservation5)
print("="*30)
animal_habitat=wildlife["habitat"].value_counts()
print(animal_habitat)
mean_observation=wildlife['observation_count'].mean()
print("Mean Observation")
print(mean_observation)
print("="*30)
median_observation=wildlife['observation_count'].median()
print("Median observation")
print(median_observation)
print("="*30)
mode_observation=wildlife['observation_count'].mode()
print("Most repeat")
print(mode_observation)
print("="*30)
min_observation=wildlife['observation_count'].min()
print("less observation")
print(min_observation)
print("="*30)
max_observation=wildlife['observation_count'].max()
print("most observatrion")
print(max_observation)
print("="*30)
observation_25=wildlife["observation_count"].quantile(0.25)
print("25% of observation")
print(observation_25)
print("="*30)
observation_75=wildlife["observation_count"].quantile(0.75)
print("75% of observation")
print(observation_75)
print("="*30)
total_opration=wildlife["observation_count"].agg(maximum=max,minimum=min,mean="mean",median="median",mode=lambda x:x.mode().iloc[0],Q1=lambda x:x.quantile(0.25),Q2=lambda x:x.quantile(0.75))
print("full details")
print(total_opration)
print("="*30)
#coumt cumsum and cummax
count_cumsum=wildlife["observation_count"].cumsum()
print("Cumulative Sum")
print(count_cumsum)
print("="*30)
count_max=wildlife['observation_count'].cummax()
print("Maximum Cumulative Value")
print(count_max)
print("="*30)

condition=[
    wildlife["observation_count"]>45,
    (wildlife["observation_count"]<=45)&
    (wildlife["observation_count"]>20),
    wildlife["observation_count"]<=20
      
]
choice=["High","Medium","small"]
wildlife["observation_category"]=np.select(condition,choice,default="unknown")
print(wildlife.head(3))
print("="*30)
place=wildlife[wildlife["habitat"].isin(["Savannah","Sahara"])]
print(place)
print("="*30)
special=wildlife[['animal','average_weight']]
print(special)
special2=wildlife[['animal','observation_count','observation_category']]
print(special2)
print("="*30)
special3=wildlife.loc[2,['animal','observation_category']]
print(special3)
special4=wildlife.loc[1:9,["animal","region"]]
print(special4)
special5=wildlife.iloc[0:12]
print(special5)

