# Exercise: https://www.hackerrank.com/challenges/itertools-combinations
from itertools import combinations

word, s = input().split()
k = int(s)
sorted_word = [x for x in word]
sorted_word.sort()


for i in range(1,k+1):
    # use combinations to create a list of all possible combinations, up to size i
    combinations_obj = list(combinations(sorted_word, i))
    for item in combinations_obj:
        print("".join(item))
