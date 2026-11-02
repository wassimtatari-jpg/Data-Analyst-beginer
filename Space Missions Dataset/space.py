import pandas as pd

import matplotlib.pyplot as plt

#read csv by pandas
space_mission=pd.read_csv('space.csv',sep=';')

#show 5 rows
print("5 rows show")
print(space_mission.head(5))
print("="*60)
#add new colum
space_mission['mission_decade']=space_mission['year']//10*10
print(space_mission.head(2))
print("="*60)
#mision sort by year
sort_mission=space_mission.sort_values('year',ascending=True)
print(sort_mission)
print("="*60)
#misiom sort by duration 
sort_duration=sort_mission.sort_values('duration_days',ascending=False)
print(sort_duration)
print("="*60)
#show special colum
special_colum=space_mission[['mission','country']]
print(special_colum)
print("="*60)
special_colum2=sort_mission[['mission','year','crew_size']]
print(special_colum2)
print("="*60)
#use condition
mission_after_2000=space_mission[space_mission['year']>2000]
print("Mission after 2000")
print("-"*60)
print(mission_after_2000)
print("="*60)
mission_crew_size_biger_0=space_mission[space_mission['crew_size']>0]
print("Mission crew size bigger than 0")
print("-"*60)
print(mission_crew_size_biger_0)
print("="*60)
success_mission=space_mission[space_mission['success']==True]
print("Success Mission")
print('-'*60)
print(success_mission)
print("="*60)
#use_index
special_index=space_mission.iloc[2:7]
print(special_index)

