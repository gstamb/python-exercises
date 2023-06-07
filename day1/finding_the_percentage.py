# Exercise: https://www.hackerrank.com/challenges/finding-the-percentage
from statistics import mean

if __name__ == '__main__':
    # Input the number of students
    num_students  = int(input())

    # Create a dictionary to store student marks
    student_marks = {}

    # Input the names and scores of the students
    for _ in range(num_students ):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    # Input the name of the student to query
    query_name = input()

    # Calculate the average score for the queried student
    to_print = mean(student_marks[query_name])

    # Print the average score with two decimal places
    print(f'{to_print:.2f}')