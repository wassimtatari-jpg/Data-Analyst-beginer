import matplotlib.pyplot as plt

months=["jan","feb","mar","apr","May","jun"]
trips=[120,150,135,180,210,190]

months.append("july")
trips.append(230)
plt.plot(months,trips,color="green")

plt.title("Monthly Trips")
plt.xlabel("months")
plt.ylabel("Trips")
plt.yticks([0,50,100,150,200,250])
plt.show()