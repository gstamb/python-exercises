# Exercise: https://www.hackerrank.com/challenges/re-findall-re-finditer/
import re

string = input()
pattern = r'(?<=[^aeiouAEIOU\s])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU\s])'
matches = re.findall(pattern, string)

if matches:
    for match in matches:
        if match is None:
            print(-1)
        else:
            print(match)
else:
    print(-1)