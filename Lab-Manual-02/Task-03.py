students = (
    ("Taukir", 28, 85),
    ("Ahmed", 24, 78),
    ("Mehedi", 20, 72),
    ("Hasan", 23, 88),
    ("Tayeb", 49, 90)

)

sorted_students = tuple(sorted(students, key = lambda  student: student[2]))
for students in sorted_students:
    print(students)