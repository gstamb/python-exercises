def validation(input_string: str):
    """
    Function that performs various validations on a given string.

    Args:
        input_string (str): The string to be validated.

    Prints:
        True if the specific validation condition is met, otherwise False.
    """
    # Check if the string has any alphanumeric characters
    for char in input_string:
        if char.isalnum():
            print(True)
            break
    else:
        print(False)

    # Check if the string has any alphabetical characters
    for char in input_string:
        if char.isalpha():
            print(True)
            break
    else:
        print(False)

    # Check if the string has any digits
    for char in input_string:
        if char.isdigit():
            print(True)
            break
    else:
        print(False)

    # Check if the string has any lowercase characters
    for char in input_string:
        if char.islower():
            print(True)
            break
    else:
        print(False)

    # Check if the string has any uppercase characters
    for char in input_string:
        if char.isupper():
            print(True)
            break
    else:
        print(False)


if __name__ == '__main__':
    # Prompt the user to input the string
    s = input()

    # Perform validations on the string
    validation(s)
