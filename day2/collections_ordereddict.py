# Exercise: https://www.hackerrank.com/challenges/py-collections-ordereddict
from collections import OrderedDict

items_sold = int(input())
# user ordered dict to maintain the order of insertion
ordered_dictionary = OrderedDict()

for _ in range(items_sold):
    line = input()
    key = line[:line.rfind(" ")]
    value = int(line[line.rfind(" ") + 1:])

    if key in ordered_dictionary:
        ordered_dictionary[key] += value
    else:
        ordered_dictionary[key] = value

for key, value in ordered_dictionary.items():
    print(key, value)