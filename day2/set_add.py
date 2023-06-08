# Exercise: https://www.hackerrank.com/challenges/py-set-add
distinct_country_stamps = set()
# for _ in range(int(input())):
#     distinct_country_stamps.add(input().strip())
# print(len(distinct_country_stamps))

# with list comprehension
[distinct_country_stamps.add(input().strip()) for x in range(int(input()))]
print(len(distinct_country_stamps))