""" Advent of Code 2024 -- Day 7 -- """
year = 2024
day = 7     # set day!

import sys
sys.path.append('../../aux')
import aoc
from math import prod, log10, ceil


def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    equations = []
    
    for line in lines:
        parts = line.split()
        res = int(parts[0][:-1])
        equations.append((res, [int(n) for n in parts[1:]]))

    return equations

def test(target, ops):
    # test for part 1
    if len(ops) == 1:
        return target == ops[0]
    else:
        if target % ops[-1] == 0:
            cond1 = test(target//ops[-1], ops[:-1])
        else :
            cond1 = False
        
        cond2 = test(target-ops[-1], ops[:-1])

        return cond1 or cond2

def test2(target, ops):
    # test for part 2
    if len(ops) == 1:
        return target == ops[0]
    else:
        if target % ops[-1] == 0:
            cond1 = test2(target//ops[-1], ops[:-1])
        else :
            cond1 = False

        cond2 = test2(target-ops[-1], ops[:-1])
        
        e = ceil(log10(ops[-1]+1))
        if (target - ops[-1]) % 10**e == 0:
            cond3 = test2( (target - ops[-1])//10**e, ops[:-1])
        else :
            cond3 = False

        return cond1 or cond2 or cond3

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    lines = parsing(data)

    # Part I    

    ans1 = 0

    for line in lines:
        # sanity checks
        if 1 not in line[1] and prod(line[1]) < line[0]:
            continue
        if test(line[0], line[1]):
            ans1 += line[0]
        
    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    
    for line in lines:
        if test2(line[0], line[1]):
            ans2 += line[0]
    
    print(f'Answer to part 2: {ans2}')
