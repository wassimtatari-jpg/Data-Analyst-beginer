import matplotlib.pyplot as plt

years=[2015,2016,2017,2018,2019,2020]
prices=[8000,8500,9900,10500,11800,15000]

change=plt.plot(years,prices)
plt.show()

change_2=plt.scatter(years,prices)
plt.xscale("log")
plt.show()

