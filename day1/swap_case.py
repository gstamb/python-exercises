# Exercise: https://www.hackerrank.com/challenges/swap-case
def swap_case(user_string):
    """
    The function takes a string and return a string with reverse letters case
    """
    # List comprehension that converts lower case letters to upper and vice versa
    return_str = ''.join([x.capitalize() if x.islower() else x.lower() for x in user_string])
    return return_str


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
