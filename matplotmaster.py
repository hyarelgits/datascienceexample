import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Marks": [85,90,45,70,35,95,60]
})

plt.hist(df["Marks"], bins=5)

plt.title("Student Marks Analysis")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.grid(True)

plt.show()
