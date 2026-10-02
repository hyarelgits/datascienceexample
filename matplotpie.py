import matplotlib.pyplot as plt

sizes = [40, 30, 20, 10]

labels = ["IT", "HR", "Finance", "Sales"]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")

plt.show()
