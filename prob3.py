import pandas as pd

df = pd.DataFrame({
    "Marks": [85, 90, 45, 70, 35, 95, 60]
})

passing_students = len(df[df["Marks"] >= 40])

total_students = len(df)

probability = passing_students / total_students

print(probability)
