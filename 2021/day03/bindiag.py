""" Advent of Code 2021 -- Day 03 -- """

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

if __name__ == '__main__':
    
    # Part I    
    data = aoc.get_input('input1.txt')                                  
    lines = data.splitlines()
    
    n = len(lines[0])
    counters = np.zeros(n)
    
    for line in lines:
        for j, c in enumerate(line):
            counters[j] += int(c)
    
    gamma = 0
    epsilon = 0
    for j, val in enumerate(counters):
        print(val, )
        if val > len(lines)//2:
            gamma += 2**(n-j-1)
        else:
            epsilon += 2**(n-j-1)
    
    ans1 = gamma*epsilon
    print(f'Answer to part 1: {ans1}')

    # Part II
    # data = aoc.get_input('input2.txt')
    
    ans2 = 0
    print(f'Answer to part 2: {ans2}')
