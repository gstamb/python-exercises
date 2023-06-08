# Exercise https://www.hackerrank.com/challenges/py-set-mutations
_ = int(input())
first_set = {int(x) for x in input().strip().split()}
operations = int(input())
for _ in range(operations):
    instruction, _ = input().strip().split()
    next_set = {int(x) for x in input().strip().split()}
    match instruction.strip().lower():
        case "intersection_update":
            first_set.intersection_update(next_set)
        case "update":
            first_set.update(next_set)
        case "symmetric_difference_update":
            first_set.symmetric_difference_update(next_set)
        case "difference_update":
            first_set.difference_update(next_set)

print(sum(first_set))
