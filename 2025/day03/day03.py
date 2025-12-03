""" Advent of Code 2025 -- Day 3 -- """
year = 2025
day = 3         # set day!

import sys
sys.path.append('../../aux')
import aoc
# import functools
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    return lines

# @functools.cache
def max_jault(s, k):
    if k == 2:
        max1 = 0
        max0 = int(s[-1])
        for j, c in enumerate(s[:-1]):
            z = int(c)
            if z > max1:
                max1 = z
                max0 = int(line[-1])
            elif z > max0:
                max0 = z
        out = 10*max1 + max0
    else :
        maxk = 0
        for j, c in enumerate(s[:-k+1]):
            z = int(c)
            if z > maxk:
                maxk = z
                val_loc = max_jault(s[j+1:],k-1)
        out = 10**(k-1)*maxk + val_loc

    return out



if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input0.txt')
    
    lines = parsing(data)

    # Part I    

    ans1 = 0

    l = len(lines)

    for line in lines:
        max1 = 0
        max0 = int(line[-1])
        for j, c in enumerate(line[:-1]):
            z = int(c)
            if z > max1:
                max1 = z
                max0 = int(line[-1])
                pos1 = j
            elif z > max0:
                max0 = z
                pos0 = j
        ans1 += 10*max1 + max0
    
    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    for line in lines:
        ans2 += max_jault(line, 12)

    
    print(f'Answer to part 2: {ans2}')
