import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Month": [1,2,3,4],
    "Sales": [100,200,150,300]
})

plt.plot(df["Month"], df["Sales"])

plt.show()
