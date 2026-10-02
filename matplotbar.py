import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English"]
marks = [85, 90, 75]

plt.bar(subjects, marks)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()
