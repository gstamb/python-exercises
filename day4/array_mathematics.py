# Exercise: https://www.hackerrank.com/challenges/np-array-mathematics
import numpy

n, m = input().split()

a_arr = []
b_arr = []
for _ in range(int(n)):
    a_arr.append([int(x) for x in input().split()])

for _ in range(int(n)):
    b_arr.append([int(x) for x in input().split()])


np_arr_a = numpy.array(a_arr)
np_arr_b = numpy.array(b_arr)

# addition
print(np_arr_a + np_arr_b)

# substraction
print(np_arr_a- np_arr_b)

# multiplication
print(np_arr_a * np_arr_b)

# integer division
print(np_arr_a // np_arr_b)

# mod
print(np_arr_a % np_arr_b)

# power
print(np_arr_a ** np_arr_b)