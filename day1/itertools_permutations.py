# Exercise: https://www.hackerrank.com/challenges/itertools-permutations
from itertools import permutations

word, s = input().split()
chars = [x for x in word]

# use itertools permutations functions to count the successive length permutations of elements in an iterable.
permutations_obj = permutations(chars, int(s))

result_list = []
for i in permutations_obj:
    result_list.append("".join(i))

result_list.sort()

for i in result_list:
    print(i)
