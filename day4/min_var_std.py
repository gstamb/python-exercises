# Exercise: https://www.hackerrank.com/challenges/np-mean-var-and-std
import numpy as np

arr_a = []
arr_b = []
N = int(input())
for _ in range(N):
    arr_a.append([int(x) for x in input().split()])

for _ in range(N):
    arr_b.append([int(x) for x in input().split()])

arr_num_a = np.array(arr_a)
arr_num_b = np.array(arr_b)


print(np.dot(arr_num_a, arr_num_b))

