# Exercise https://www.hackerrank.com/challenges/np-concatenate
import numpy

n, m , p = input().split()

array_1 = []
array_2 = []
for i in range(int(n)):
    array_1.append([int(x) for x in input().split()])

for i in range(int(m)):
    array_2.append([int(x) for x in input().split()])

numpy_array1 = numpy.array(array_1)
numpy_array2 = numpy.array(array_2)

print(numpy.concatenate((numpy_array1, numpy_array2), axis=0))