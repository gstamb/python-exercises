import numpy

N, M = input().split()

arr = []

for i in range(int(N)):
    arr.append([int(x) for x in input().split()])

np_array = numpy.array(arr)
sum_along_0 = numpy.sum(np_array, axis=0)
product = numpy.prod(sum_along_0)
print(product)