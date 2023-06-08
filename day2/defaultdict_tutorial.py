# Exercise: https://www.hackerrank.com/challenges/defaultdict-tutorial/

from collections import defaultdict

# Read input values
n, m = [int(x) for x in input().split()]

# Create a defaultdict to store the indices of words in group A
indices = defaultdict(list)

# Read group A words and store their indices
for i in range(1, n + 1):
    word = input()
    indices[word].append(str(i))

# Process group B words
for _ in range(m):
    word = input()
    # Check if the word exists in group A
    if word in indices:
        print(' '.join(indices[word]))
    else:
        print(-1)
