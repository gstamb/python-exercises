# Exercise: https://www.hackerrank.com/challenges/python-string-formatting


def print_formatted(number):
    """ The function prints the Decimal, Octal, Hexadecimal (capitalized) and Binary representation of a `1-N`"""
    arr = []
    for i in range(1, number + 1):
        decimal = str(i)
        octal = str(oct(i)[2:])
        r = str(hex(i))[2:].capitalize()
        hexadecimal = ''.join([x.capitalize() for x in r])
        binary = str(bin(i))[2:]
        arr.append([decimal, octal, hexadecimal, binary])
    column1 = len(arr[number - 1][0])
    column2 = len(arr[number - 1][1])
    column3 = len(arr[number - 1][2])
    column4 = len(arr[number - 1][3])
    for i in arr:
        print(f'{i[0].rjust(column4)} {i[1].rjust(column4)} {i[2].rjust(column4)} {i[3].rjust(column4)}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
