# Exercise: https://www.hackerrank.com/challenges/designer-door-mat
# Draw a figure

# Size: 7x21
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME - ------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------

# take input
n, m = [int(x) for x in input().split()]

# drow top part
for i in range(1, ((n - 1) // 2) * 2, 2):
    symbol = '.|.' * (i)
    print('-' * ((m - len(symbol)) // 2) + symbol + '-' * ((m - len(symbol)) // 2))

# draw middle part
print('-' * ((m - 7) // 2) + 'WELCOME' + '-' * ((m - 7) // 2))

# draw bottom part
for i in range(((n - 1) // 2) * 2, 1, -2):
    symbol = '.|.' * (i - 1)
    print('-' * ((m - len(symbol)) // 2) + symbol + '-' * ((m - len(symbol)) // 2))
