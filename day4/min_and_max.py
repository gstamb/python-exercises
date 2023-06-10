# Exercise: https://www.hackerrank.com/challenges/np-min-and-max
import numpy

arr = []

for _ in range(int(input()[0])):
    arr.append([int(x) for x in input().split()])

arr_num = numpy.array(arr)
x_min = numpy.min(arr_num, axis=1)
result = numpy.max(x_min)
print(result)
