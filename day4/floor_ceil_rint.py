# Exercise # https://www.hackerrank.com/challenges/floor-ceil-and-rint
import numpy

numpy.set_printoptions(legacy='1.13')
arr = numpy.array([x for x in input().split()], float)

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
