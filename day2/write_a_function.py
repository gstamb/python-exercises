# https://www.hackerrank.com/challenges/write-a-function

def is_leap(year):
    """
    Check if a given year is a leap year.

    Args:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    leap = False

    # Check if the year is divisible by 4
    if year % 4 == 0:

        # Check if the year is divisible by 100
        if year % 100 == 0:

            # Check if the year is divisible by 400
            if year % 400 == 0:
                leap = True
            else:
                return leap

        leap = True

    return leap
