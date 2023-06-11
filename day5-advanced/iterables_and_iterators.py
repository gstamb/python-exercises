# Exercise: https://www.hackerrank.com/challenges/iterables-and-iterators
from itertools import combinations

N = int(input())
arr = "".join([x for x in input().split()])
lenght = int(input())

combs = tuple(combinations(arr, lenght))
cnt = 0
for i in combs:
    if "a" in i:
        cnt += 1


print(round(cnt/len(tuple(combs)),4))