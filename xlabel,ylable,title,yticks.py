import matplotlib.pyplot as plt

year=[1950,1951,1952,2100]
pop=[2.53,2.65,2.90,10.25]

year=[1800,1850,1900]+year
pop=[1.25,1.55,1.95]+pop
plt.plot(year,pop)

plt.xlabel("years")
plt.ylabel("population")
plt.title("world population projections")
plt.yticks([0,2,4,6,8,10],
           ['0','2B','4B',"6B","8B","10B"])



plt.show()