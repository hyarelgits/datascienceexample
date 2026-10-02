import pandas as pd

data = {
    "EmpID": [101, 102, 103],
    "Name": ["John", "David", "Smith"],
    "Department": ["IT", "HR", "IT"],
    "Salary": [50000, 45000, 60000]
}

df = pd.DataFrame(data)

df.to_csv("employees.csv", index=False)

print("Excel file created successfully!")
