import statistics
import numpy as np
marks = [85, 90, 45, 70, 35, 95, 60]
range_value = max(marks) - min(marks)
print("Sum     :", sum(marks))
print("Count   :", len(marks))
print("Mean    :", statistics.mean(marks))
print("Median  :", statistics.median(marks))
print("Maximum :", max(marks))
print("Minimum :", min(marks))
print(statistics.mode(marks))
print(range_value)
print(np.var(marks))
print(np.std(marks))
