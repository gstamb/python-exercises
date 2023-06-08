# Exercise: https://www.hackerrank.com/challenges/zipped/
students, marks = [int(x) for x in input().split()]
subject = []
for i in range(marks):
     next_subject = [float(x) for x in input().split()]
     subject.append(next_subject)

transposed_grades = zip(*subject)
for student_grades in transposed_grades:
    print(sum(student_grades)/len(student_grades))