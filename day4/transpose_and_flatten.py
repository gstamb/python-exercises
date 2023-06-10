# Exercise: https://www.hackerrank.com/challenges/np-transpose-and-flatten/
import numpy

n, m = input().split()

myarr = numpy.empty((0,int(m)))

for i in range(int(n)):
    myarr = numpy.vstack((myarr, numpy.array([int(x) for x in input().split()])))


print(myarr.transpose())
print(myarr.flatten())
