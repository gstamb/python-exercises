# Exercise: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement

from itertools import combinations_with_replacement

word, s = input().split()
k = int(s)
sorted_word = [x for x in word]
sorted_word.sort()

#  use combinations_with_replacement to allow combinations to be repeated more than once
possible_replacements = list(combinations_with_replacement(sorted_word,k))

for item in possible_replacements:
    print(''.join(item))

