# Exercise: https://www.hackerrank.com/challenges/most-commons
from collections import Counter

if __name__ == '__main__':
    s = input()
    sorted_str = sorted(s)
    c = Counter(sorted_str)

    result = c.most_common(3)

    for i in result:
        print(i[0], i[1])