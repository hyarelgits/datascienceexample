import pandas as pd

df = pd.DataFrame({
"Name": ["A", "B", "C"],
"Salary": [50000, 70000, 90000]
})


print(df)

data = [
[1, "A"],
[2, "B"],
[3, "C"]
]


df1 = pd.DataFrame(data,
columns=["ID", "Name"])

print(df1)
