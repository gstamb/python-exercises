# Exercise: https://www.hackerrank.com/challenges/py-introduction-to-sets

def average(array):
    set_contents = set(array)
    return sum(set_contents) / len(set_contents)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
