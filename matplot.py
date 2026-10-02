import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Marks": [85, 90, 45, 70, 35, 95, 60]
})

plt.hist(df["Marks"])
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.show()
