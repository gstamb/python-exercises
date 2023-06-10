# Exercise: https://www.hackerrank.com/challenges/np-shape-reshape
import numpy

arr = [x for x in input().split()]

my_array = numpy.array(arr, int)
print(my_array.reshape(3, 3))
