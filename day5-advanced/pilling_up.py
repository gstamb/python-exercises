# Exercise: https://www.hackerrank.com/challenges/piling-up/

for _ in range(int(input())):
    _ = input()
    arr = list(map(int, input().split()))
    max_element = max(arr)
    while (arr):
        if arr[0] >= arr[-1]:
            current_highest = arr.pop(0)
        else:
            current_highest = arr.pop(-1)
        if max_element >= current_highest:
            max_element = current_highest
        else:
            print("No")
            break
    else:
        print("Yes")
