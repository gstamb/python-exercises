# Exercise: https://www.hackerrank.com/challenges/collections-counter
from collections import Counter

count_shoes = int(input())
# use collection Counter class to count the amount of shoe pairs
shoe_sizes = Counter([int(x) for x in input().split()])
count_customers = int(input())

cash = 0
for customer in range(count_customers):
    size, price = input().split()
    if shoe_sizes[int(size)] > 0:
        shoe_sizes[int(size)] -= 1
        cash += int(price)

print(cash)
