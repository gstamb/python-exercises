# Exercise: https://www.hackerrank.com/challenges/py-check-subset
test_cases = int(input())

for _ in range(test_cases):
    _ = input()
    set_1 = {int(x) for x in input().split()}
    _ = input()
    set_2 = {int(x) for x in input().split()}
    print(set_1.issubset(set_2))
