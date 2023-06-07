# Exercise: https://www.hackerrank.com/challenges/itertools-product
from itertools import product

input_1 = input()
input_2 = input()

tuple_1 = tuple([int(x) for x in input_1.split()])
tuple_2 = tuple([int(x) for x in input_2.split()])

# use itertools product function to create a cartesian product of two tuples
cartesian = product(tuple_1, tuple_2)

for i in cartesian:
    print(i, end=' ')
