# Exercise: https://www.hackerrank.com/challenges/py-set-union

english_paper = input()
english_subscribers = set([x for x in input().split()])
french_paper = input()
french_subscribers = set([x for x in input().split()])
set_union = english_subscribers.union(french_subscribers)
print(len(set_union))
