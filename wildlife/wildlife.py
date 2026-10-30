import pandas as pd

wild_life=pd.read_csv("wildlife.csv",sep=";")
print(wild_life.head())
print("-"*30)

population=wild_life.sort_values('population',ascending=True)
print(population)
print("-"*30)
av_weight=wild_life.sort_values("average_weight",ascending=False)
print(av_weight)
print("-"*30)
animal_more_100=wild_life[wild_life["population"]>100]
print(animal_more_100)
animal_less_60=wild_life[wild_life["population"]<60]
print(animal_less_60)
place_live=wild_life[wild_life["habitat"].isin(["Forest","Savannah"])]
print(place_live)
habitat=wild_life["habitat"].isin(["Forest"])
print(habitat)
sort_habitat=wild_life[habitat]
print(sort_habitat)
check_value=wild_life.isin(["Savannah",'Forest','Endangered'])
print(check_value)
