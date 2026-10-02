import pandas as pd

df = pd.read_csv("employees.csv")

print(df)

print(df.head(1))
print(df.tail(1))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())
print(df["EmpID"])
print(df.loc[2])
print(df.loc[0:2, ["EmpID", "Salary"]])
print(df.iloc[1])
print(df[df["Salary"] > 45000])
print(df["Salary"].mean())
print(df["Salary"].isnull())
print(df.groupby("Department")["Salary"].mean())

