# Exercise: https://www.hackerrank.com/challenges/python-string-split-and-join
def split_and_join(line: str) -> str:
    """
    Function receives a string and replaces separator
    """
    split_words = line.split()
    rejoin_words = "-".join(split_words)
    return rejoin_words
