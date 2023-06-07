# Exercise: https://www.hackerrank.com/challenges/list-comprehensions
if __name__ == '__main__':
    # Prompt the user to input four integers
    x = int(input("Enter the value for x: "))
    y = int(input("Enter the value for y: "))
    z = int(input("Enter the value for z: "))
    n = int(input("Enter the value for n: "))

    # Generate a list of lists containing all possible combinations of a, b, and c
    lc = [[a, b, c] for a in range(x + 1)
          for b in range(y + 1)
          for c in range(z + 1)
          if a + b + c != n]

    # Print the resulting list
    print(lc)
