import matplotlib.pyplot as plt

plt.subplot(1,2,1)
plt.plot([1,2,3],[10,20,30])
plt.title("Chart 1")

plt.subplot(1,2,2)
plt.plot([1,2,3],[30,20,10])
plt.title("Chart 2")

plt.show()
