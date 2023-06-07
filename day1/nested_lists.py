# Exercise: https://www.hackerrank.com/challenges/nested-list

if __name__ == '__main__':
    student_list = []

    # Input the number of students
    num_students = int(input())

    # Input the names and scores of the students
    for _ in range(num_students):
        name = input()
        score = float(input())
        student_list.append([name, score])

    # Sort the student_list based on scores in ascending order, and then by names in alphabetical order
    sorted_students = sorted(student_list, key=lambda student: (student[1], student[0]))

    # Find the second lowest score
    second_lowest_score = sorted(set(score for _, score in sorted_students))[1]

    # Iterate over the sorted_students list
    for item in sorted_students:
        # If the score of the current item is equal to the second lowest score
        if item[1] == second_lowest_score:
            # Print the name of the student
            print(item[0])
