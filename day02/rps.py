"""
Advent of Code 2022
Day 02
"""

# import numpy as np

# read input
with open('input.txt', 'r') as file:
    data = file.read()


def score(strategy):
    
    opp = {}
    opp['A'] = 1
    opp['B'] = 2
    opp['C'] = 3
    
    my = {}
    my['X'] = 1
    my['Y'] = 2
    my['Z'] = 3
    
    strats = strategy.split()

    return my[strats[-1]]

total_score = 0

for line in data.splitlines():
    pts = score(line)
    total_score += pts
    print(line.split(), pts)

print(f'Total score is {total_score}')
