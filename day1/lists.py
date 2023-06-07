# Exercise: https://www.hackerrank.com/challenges/python-lists

if __name__ == '__main__':
    N = int(input())
    data = []
    for i in range(N):
        # perform operation depending on user input
        action = [x for x in input().split()]
        if action[0].lower() == 'insert':
            data.insert(int(action[1]), int(action[2]))
        elif action[0].lower() == 'delete':
            data.remove(int(action[1]))
        elif action[0].lower() == 'append':
            data.append(int(action[1]))
        elif action[0].lower() == 'sort':
            data.sort()
        elif action[0].lower() == 'pop':
            data.pop()
        elif action[0].lower() == 'reverse':
            data.reverse()
        elif action[0].lower() =='remove':
            data.remove(int(action[1]))
        elif action[0].lower() == 'print':
            print(data)
