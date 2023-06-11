# Exercise: https://www.hackerrank.com/challenges/ginorts

# string = input()
# lowercase = [x for x in string if x.islower()]
# uppercase = [x for x in string if x.isupper()]
# digits = [x for x in string if x.isdigit()]
#
# result = sorted(lowercase) + sorted(uppercase) + sorted([x for x in digits if int(x) % 2 == 1])+sorted([x for x in digits if int(x) % 2 == 0])
# print("".join(result))

def custom_sort(char):
    if char.islower():
        return (1, char)
    elif char.isupper():
        return (2, char)
    elif char.isdigit():
        if int(char) % 2 == 1:
            return (3, char)
        else:
            return (4, char)

input_string = input()
sorted_string = ''.join(sorted(input_string, key=custom_sort))
print(sorted_string)