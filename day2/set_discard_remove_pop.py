# Exercies: https://www.hackerrank.com/challenges/py-set-discard-remove-pop

n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    command = input().split()
    if len(command) == 1:
        s.pop()
    else:
        action = command[0]
        index = int(command[1])
        if action.lower() == "discard":
            s.discard(index)
        else:
            s.remove(index)
print(sum(s))