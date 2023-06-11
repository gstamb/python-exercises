# Exercise: https://www.hackerrank.com/challenges/no-idea
n, m = map(int, input().split())
arr = [int(x) for x in input().split()]
set_a = {int(x) for x in input().split()}
set_b = {int(x) for x in input().split()}

happiness = 0
for i in range(len(arr)):
    if arr[i] in set_a:
        happiness += 1
    if arr[i] in set_b:
        happiness -= 1

print(happiness)
