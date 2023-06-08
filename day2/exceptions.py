# Exercise: https://www.hackerrank.com/challenges/exceptions
def divide(x, y):
    x = int(x)
    y = int(y)
    print(int(x / y))


number_inputs = int(input())

for inputs in range(number_inputs):
    first_num, second_num = input().split()
    try:
        divide(first_num, second_num)
    # Hard coded the errors because it appears that HR uses older version of python
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)
