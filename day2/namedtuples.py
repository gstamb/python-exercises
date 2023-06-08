# Exercise: https://www.hackerrank.com/challenges/py-collections-namedtuple
from collections import namedtuple

# Define the named tuple
Student = namedtuple('Student', 'MARKS')

data = []
index = 0

for i in range(int(input()) + 1):
    field_names = [x.strip() for x in input().split()]

    # Get field index
    if i == 0:
        index = field_names.index("MARKS")
    else:
        # Create a named tuple instance and add it to the data list
        student = Student(int(field_names[index]))
        data.append(student)

# Calculate the sum of grades and number of students
sum_grades = sum(student.MARKS for student in data)
num_students = len(data)

# Print the average grade with two decimal places
average_grade = sum_grades / num_students
print("{:.2f}".format(average_grade))