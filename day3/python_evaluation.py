# Exercise: https://www.hackerrank.com/challenges/python-eval/
string_input = input()
result = eval(string_input)
if result is not None:
    print(result)