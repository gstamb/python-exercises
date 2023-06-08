# Exercise: https://www.hackerrank.com/challenges/py-collections-deque
from collections import deque

d = deque()
for _ in range(int(input())):
    command = input()

    if command == "pop":
        d.pop()
    elif command == "popleft":
        d.popleft()
    elif command.startswith("appendleft"):
        value = command.split()[1]
        d.appendleft(int(value))
    else:
        value = command.split()[1]
        d.append(int(value))

[print(x, end=" ") for x in d]
