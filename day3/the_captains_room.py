# Exercise: https://www.hackerrank.com/challenges/py-the-captains-room
from collections import Counter
group_size = int(input())
room_allocation = [x for x in input().split()]
c = Counter(room_allocation)
for item in c:
    if c[item] == 1 :
        print(item)