""" Advent of Code 2023 -- Day 09 -- """

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def parsing(data):
    # write parser of input data    
    lines = data.splitlines()
    
    numbers = []

    for line in lines:
        nums = np.array([int(n) for n in line.split()], dtype=int)
        numbers.append(nums)        

    return numbers

def take_diff(nums):
    lvl = 0
    diffs = []
    diffs.append(nums)
    while np.any(diffs[lvl]!=0):
        diffs.append(np.diff(diffs[lvl]))
        lvl += 1

    return diffs

def extrap(diffs):
    # for part I
    lvl = len(diffs)
    
    extr = 0
    for l in range(lvl-1):
        extr = diffs[lvl-2-l][-1] + extr
    
    return extr

def extrap2(diffs):
    # for part II
    lvl = len(diffs)
    
    extr = 0
    for l in range(lvl-1):
        extr = diffs[lvl-2-l][0] - extr
    
    return extr

if __name__ == '__main__':
    data = aoc.get_input('input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    numbers = parsing(data)

    # Part I    
    
    ans1 = 0
    
    for nums in numbers:
        diffs = take_diff(nums)

        extr = extrap(diffs)
        ans1 += extr
            
    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    
    for nums in numbers:
        diffs = take_diff(nums)

        extr = extrap2(diffs)
        ans2 += extr

    print(f'Answer to part 2: {ans2}')
