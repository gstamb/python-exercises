# Exercise: https://www.hackerrank.com/challenges/introduction-to-regex
import re

inputs = int(input())
pattern = r'^[+-]?(\d+(\.\d+)?|\.\d+)$'

for _ in range(inputs):
    string_to_check = input()
    m = re.search(pattern, string_to_check)
    if string_to_check.isdigit():
        if int(string_to_check) == 0:
            print(False)
            continue
    if m:
        print(True)
    else:
        print(False)
