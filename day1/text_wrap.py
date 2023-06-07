# Exercise: https://www.hackerrank.com/challenges/text-wrap

import textwrap


def wrap(string_input, max_width):
    """
    Wrap long lines of text to a columns of predefined width
    """
    text = textwrap.fill(string_input, width=max_width)
    return text


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
