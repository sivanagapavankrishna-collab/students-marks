


# Student Marks Matrix Analysis

marks = [
    [85, 90, 75],
    [70, 65, 80],
    [95, 92, 98],
    [40, 45, 50]
]

students = ["Pavan", "Ravi", "Arjun", "Kiran"]
subjects = ["Python", "Maths", "English"]

# Row-wise analysis
print("Student Performance:")

for i in range(len(marks)):
    total = sum(marks[i])
    avg = total / len(subjects)

    print(students[i], "Total:", total, "Average:", avg)

# Find top performer
top = max(range(len(marks)),
          key=lambda i: sum(marks[i]))

print("\nTop Performer:", students[top])

# Column-wise analysis
print("\nSubject Performance:")

for j in range(len(subjects)):
    total = 0

    for i in range(len(marks)):
        total += marks[i][j]

    avg = total / len(students)

    print(subjects[j], "Average:", avg)

    if avg < 50:
        print("Low Performance Subject:", subjects[j])

