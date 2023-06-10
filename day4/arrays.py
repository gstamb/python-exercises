# Exercise: https://www.hackerrank.com/challenges/np-arrays
import numpy


def arrays(arr):
    a = numpy.array(arr, float)[::-1]
    return a


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
