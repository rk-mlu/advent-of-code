""" Advent of Code 2021 -- Day 06 -- """
year = 2021
day = 6     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
from collections import Counter

def parsing(data):
    # parser for the input data    
    nums = [int(n) for n in data.split(',')]

    return np.array(nums, dtype=int)

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    fishs = parsing(data)

    c = Counter(fishs)
    c[0] = 0
    c[7] = 0
    c[8] = 0
    print(c)

    # Part I    
    
    days = 80

    for day in range(days):
        new_c = dict()
        
        for k in range(8):
            new_c[k] = c[k+1]
        new_c[6] += c[0]
        new_c[8] = c[0]
        c = new_c
    
    ans1 = 0

    for k in range(9):
        ans1 += c[k]

    print(f'Answer to part 1: {ans1}')

    # Part II
    c = Counter(fishs)
    c[0] = 0
    c[7] = 0
    c[8] = 0
    
    days = 256

    for day in range(days):
        new_c = dict()
        
        for k in range(8):
            new_c[k] = c[k+1]
        new_c[6] += c[0]
        new_c[8] = c[0]
        c = new_c
    
    ans2 = 0

    for k in range(9):
        ans2 += c[k]
    
    print(f'Answer to part 2: {ans2}')
