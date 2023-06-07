# Exercise: https://www.hackerrank.com/challenges/python-mutations
def mutate_string(string, position, character):
    """
    Function that changes a string
    """
    # convert the string to list of chars
    char_list = [x for x in string]

    # assigns the char position within list
    position = int(position)

    # changes the char
    char_list[position] = character

    # rejoins the chars
    return_str = ''.join(char_list)
    return return_str


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)