# Exercise: https://www.hackerrank.com/challenges/find-a-string
def count_substring(input_string: str, sub_string: str) -> int:
    """
    Function that finds the occurrences of a substring within a string.

    Args:
        input_string (str): The string in which the occurrences of the substring will be counted.
        sub_string (str): The substring whose occurrences will be counted within the input string.

    Returns:
        int: The number of occurrences of the substring within the input string.
    """
    count = 0
    for i in range(len(input_string) - len(sub_string) + 1):
        current_str = input_string[i:i + len(sub_string)]
        if current_str == sub_string:
            count += 1

    return count


if __name__ == '__main__':
    # Prompt the user to input the main string
    string = input().strip()

    # Prompt the user to input the substring to search for
    sub_string = input().strip()

    # Count the occurrences of the substring within the main string
    count = count_substring(string, sub_string)

    # Print the count of occurrences
    print(count)
