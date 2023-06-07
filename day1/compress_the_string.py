# Exercise: https://www.hackerrank.com/challenges/compress-the-string
from itertools import groupby

lst = input()
list_of_nums = [int(x) for x in lst]

# use group by to count occurrence  of a key
for key, group in groupby(list_of_nums):
    print((len((list(group))), key), end= ' ')