# =====================================
# STUDENT PERFORMANCE ANALYZER PROJECT
# =====================================

# Import Libraries

import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# =====================================
# STEP 1 : CREATE DATASET
# =====================================

print("\n===== STUDENT DATA =====\n")

df = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E"],
    "Math": [80, 70, 90, 60, 50],
    "Science": [85, 65, 92, 58, 55]
})

print(df)


# =====================================
# STEP 2 : PANDAS OPERATIONS
# =====================================

print("\n===== PANDAS ANALYSIS =====\n")

df["Total"] = df["Math"] + df["Science"]

df["Average"] = df["Total"] / 2

print(df)



# =====================================
# STEP 3 : STATISTICS
# =====================================

print("\n===== STATISTICS =====\n")

print("Mean      :", statistics.mean(df["Total"]))
print("Median    :", statistics.median(df["Total"]))
print("Maximum   :", max(df["Total"]))
print("Minimum   :", min(df["Total"]))





# =====================================
# STEP 4 : NUMPY OPERATIONS
# =====================================

print("\n===== NUMPY ANALYSIS =====\n")

print("Variance  :", np.var(df["Total"]))
print("Std Dev   :", np.std(df["Total"]))
print("Mean      :", np.mean(df["Total"]))
print("Sum       :", np.sum(df["Total"]))


# =====================================
# STEP 5 : PROBABILITY
# =====================================

print("\n===== PROBABILITY =====\n")

# Total >= 120 is Pass

passing_students = len(df[df["Total"] >= 120])

total_students = len(df)

pass_probability = passing_students / total_students

print("Passing Students :", passing_students)
print("Total Students   :", total_students)
print("Pass Probability :", pass_probability)

print("Pass Percentage  :", pass_probability * 100, "%")



# =====================================
# STEP 6 : MATRIX OPERATIONS
# =====================================

print("\n===== MATRIX OPERATIONS =====\n")

marks_matrix = np.array([
    [80, 85],
    [70, 65],
    [90, 92],
    [60, 58],
    [50, 55]
])

print("Matrix:\n")
print(marks_matrix)

print("\nShape :", marks_matrix.shape)

print("Rows :", marks_matrix.shape[0])

print("Columns :", marks_matrix.shape[1])

print("Matrix Sum :", np.sum(marks_matrix))

print("Matrix Mean :", np.mean(marks_matrix))




# =====================================
# STEP 7 : AI MODEL
# =====================================

print("\n===== AI MODEL =====\n")

X = df[["Math", "Science"]]

y = df["Total"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[75, 80]])

print("Predicted Total Marks for")
print("Math = 75")
print("Science = 80")

print("Prediction =", prediction[0])




# =====================================
# STEP 8 : BAR CHART
# =====================================

plt.figure(figsize=(8,5))

plt.bar(df["Student"], df["Total"])

plt.title("Student Total Marks")

plt.xlabel("Students")

plt.ylabel("Total Marks")

plt.savefig("student_bar_chart.png")

print("\nBar Chart Saved: student_bar_chart.png")


# =====================================
# STEP 9 : HISTOGRAM
# =====================================

plt.figure(figsize=(8,5))

plt.hist(df["Total"], bins=5)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Students")

plt.savefig("marks_histogram.png")

print("Histogram Saved: marks_histogram.png")


# =====================================
# STEP 10 : SCATTER PLOT
# =====================================

plt.figure(figsize=(8,5))

plt.scatter(df["Math"], df["Science"])

plt.title("Math vs Science")

plt.xlabel("Math")

plt.ylabel("Science")

plt.savefig("scatter_plot.png")

print("Scatter Plot Saved: scatter_plot.png")


print("\n===== PROJECT COMPLETED SUCCESSFULLY =====")
