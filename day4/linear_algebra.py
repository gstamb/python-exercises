# Exercise: https://www.hackerrank.com/challenges/np-linear-algebra

import numpy

N = int(input())
arr = []
for _ in range(N):
    arr.append([float(x) for x in input().split()])

print(round(numpy.linalg.det(arr),2))