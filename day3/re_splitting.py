# Exercise: https://www.hackerrank.com/challenges/re-split
import re

regex_pattern = r'(?<=\d)[,.](?=\d)'  # Do not delete 'r'.
print("\n".join(re.split(regex_pattern, input())))
