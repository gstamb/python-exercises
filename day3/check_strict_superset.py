# Exercise: https://www.hackerrank.com/challenges/py-check-strict-superset

# assuming we work with a superset we check if all conditions are met
# len(superset) > len(set_to_check) and a.issuperset(b)
superset = {x for x in input().split()}
count_sets = int(input())

ret = True

for i in range(count_sets):
    set_to_check = {x for x in input().split()}
    if superset.issuperset(set_to_check):
        if len(set_to_check) == superset:
            ret = False
        else:
            continue
    else:
        ret = False

print(ret)
