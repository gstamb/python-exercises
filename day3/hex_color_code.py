# Exercise: https://www.hackerrank.com/challenges/hex-color-code
import re

pattern = r"#[a-fA-F0-9]+(?=[;),])"

for row in range(int(input())):
    string = input()
    if string.startswith("#"):
        continue
    match = re.finditer(pattern, string)

    if re.search(pattern, string):
        for x in match:
            print(x.group())
