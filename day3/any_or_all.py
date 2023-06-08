# Exercise: https://www.hackerrank.com/challenges/any-or-all
_ = input()
arr = list(map(int, input().split()))
positive = sum(all(n > 0 for n in lst) for lst in [arr])
palindrome = sum(any(str(n) == str(n)[::-1] for n in lst) for lst in [arr])
[print(True) if positive+palindrome == 2 else print(False)]