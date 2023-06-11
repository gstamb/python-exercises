# Exercise: https://www.hackerrank.com/challenges/merge-the-tools
def merge_the_tools(string, k):
    result_string = []

    for i in range(0, len(string), k):
        b = list(x for x in string[i:i + k])
        c = list(dict.fromkeys(b))
        result_string.append("".join(c))

    for i in range(len(result_string)):
        print(result_string[i])

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)



