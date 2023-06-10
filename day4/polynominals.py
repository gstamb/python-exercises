# Exercise: https://www.hackerrank.com/challenges/np-polynomials
import numpy
arr = [float(x) for x in input().split()]
x = int(input())

print(numpy.polyval(arr, x))