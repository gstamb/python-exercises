# Exercise: https://www.hackerrank.com/challenges/capitalize

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    """
    Function that capitalizes the first letter of each word in a given string.

    Args:
        s (str): The string to be modified.

    Returns:
        str: The modified string with the first letter of each word capitalized.
    """
    new_str = ''
    prev = [i for i, ltr in enumerate(s) if ltr == ' ']

    for index, i in enumerate(s):
        if index == 0 or index - 1 in prev:
            new_str += i.capitalize()
        else:
            new_str += i

    return new_str


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
