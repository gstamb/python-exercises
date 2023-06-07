# Exercise: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
if __name__ == '__main__':
    # Prompt the user to input the value of n

    n = int(input())
    # Prompt the user to input the elements separated by space

    arr = map(int, input().split())
    # Convert the elements into a list and remove duplicates

    lst = list(set(arr))
    # Sort the unique elements in ascending order

    lst.sort()
    # Print the second largest element
    print(lst[-2])
