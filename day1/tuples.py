# Exercise: https://www.hackerrank.com/challenges/python-tuples
num_input = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(hash(t))