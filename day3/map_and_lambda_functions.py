# Exercise: https://www.hackerrank.com/challenges/map-and-lambda-expression
cube = lambda x: x * x * x  # complete the lambda function


def fibonacci(n):
    a = 0
    b = 1

    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        result = [0, b]
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            result.append(b)
        return result[0:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
