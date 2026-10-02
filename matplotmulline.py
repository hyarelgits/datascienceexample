import matplotlib.pyplot as plt

months = [1,2,3,4]

sales1 = [10,20,30,40]
sales2 = [15,25,35,45]

plt.plot(months, sales1, label="Product A")
plt.plot(months, sales2, label="Product B")

plt.legend()
plt.savefig("chart.png")
plt.show()
