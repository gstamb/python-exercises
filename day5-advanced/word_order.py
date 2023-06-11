# Exercises: https://www.hackerrank.com/challenges/word-order
from collections import OrderedDict, Counter

d = OrderedDict()
input_arr = []
for word in range(int(input())):
    input_arr.append(input())

c = Counter(input_arr)
print(len(c))
for item in c:
    print(c[item], end=" ")
