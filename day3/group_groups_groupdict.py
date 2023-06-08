# Exercise: https://www.hackerrank.com/challenges/re-group-groups
import re

pattern = r'((?!_)\w)\1+'
match = re.search(pattern, input())

if match:
    print(match.group(1))
else:
    print(-1)