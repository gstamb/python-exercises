# Exercise: https://www.hackerrank.com/challenges/np-zeros-and-ones
import numpy

nums = [int(x) for x in input().split()]

print(numpy.zeros(nums, dtype=int))
print(numpy.ones(nums, dtype=int))
