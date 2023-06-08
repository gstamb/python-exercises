# Exercise: https://www.hackerrank.com/challenges/the-minion-game/
def minion_game(string):
    """
    Determines the winner and score of the 'The Minion Game' based on the given string.

    Args:
        string (str): The string to analyze.

    Prints:
        str: The winner's name and score, separated by a space on one line, or 'Draw' if there is no winner.
    """

    vowels = 'AEIOU'
    length = len(string)
    kevin_score = 0
    stuart_score = 0

    for i in range(length):
        if string[i] in vowels:
            # If the current character is a vowel, update Kevin's score by adding the count of remaining substrings.
            kevin_score += length - i
        else:
            # If the current character is a consonant, update Stuart's score by adding
            # the count of remaining substrings.
            stuart_score += length - i

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")


# Test the function
string = input()
minion_game(string)
