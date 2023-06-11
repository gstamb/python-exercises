# Exercise: https://www.hackerrank.com/challenges/re-sub-regex-substitution
import re

pattern1 = '(?<=\s)\&\&(?=\s)'
pattern2 = '(?<=\s)\|\|(?=\s)'
for i in range(int(input())):
    print(re.sub(pattern1,'and', re.sub(pattern2, 'or', input())))