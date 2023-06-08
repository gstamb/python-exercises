# Exercise: https://www.hackerrank.com/challenges/input
x,k = input().split()
if eval(input().replace("x",x)) == int(k):
    print(True)
else:
    print(False)
