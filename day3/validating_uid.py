# Exercise: https://www.hackerrank.com/challenges/validating-uid/
import re
pattern = r"^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:.*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$"
for i in range(int(input())):
    string = input()
    match = re.search(pattern, string)

    if match:
        print("Valid")
    else:
        print("Invalid")
