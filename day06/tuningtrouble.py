""" Advent of Code 2022 -- Day 06 -- """

# read input
with open('input.txt', 'r') as file:
    data = file.read()

l = len(data)

# Part I
digits = 4

for i in range(l):
    s = set()
    for c in data[i:i+digits]:
        s.add(c)
    if len(s) == digits:
        print(f'Part I: first marker detected at {i+digits}: {data[i:i+digits]}')
        break

# Part II
digits = 14

for i in range(l):
    s = set()
    for c in data[i:i+digits]:
        s.add(c)
    if len(s) == digits:
        print(f'Part II: First start-of-message marker detected at {i+digits}')
        break
