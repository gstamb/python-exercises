# Exercise: https://www.hackerrank.com/challenges/np-eye-and-identity
import numpy
rows, columns = [int(x) for x in input().split()]

numpy.set_printoptions(legacy='1.13')
print(numpy.eye(rows, columns, k=0))
