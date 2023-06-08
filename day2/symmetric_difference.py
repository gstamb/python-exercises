# Exercise: https://www.hackerrank.com/challenges/symmetric-difference
first_int = int(input())
first_set = {int(x) for x in input().split()}
second_int = int(input())
second_set = {int(x) for x in input().split()}

# Find the symmetric difference using the ^ operator
symmetric_difference = sorted(first_set ^ second_set)

for item in symmetric_difference:
    print(item)