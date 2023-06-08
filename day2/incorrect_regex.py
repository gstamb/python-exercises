# Exercise: https://www.hackerrank.com/challenges/incorrect-regex/
import re

for _ in range(int(input())):
    pattern = input()
    try:
        a = ""
        re.match(pattern, a)  # Attempt to match an empty string
        print(True)
    except re.error:
        print(False)
