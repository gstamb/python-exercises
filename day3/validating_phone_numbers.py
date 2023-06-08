# Exercise: https://www.hackerrank.com/challenges/validating-the-phone-number
import re
pattern = r"^[987]\d{9,9}$"

for i in range(int(input())):
    string = input()
    match = re.search(pattern, string)

    if match:
        print("YES")
    else:
        print("NO")
