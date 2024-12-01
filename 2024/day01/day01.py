""" Advent of Code 2024 -- Day 01 -- """
year = 2024
day = 1     # set day!

import sys
sys.path.append('../../aux')
import aoc
from collections import Counter
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    return lines

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    lines = parsing(data)
    
    left = []
    right = []

    for line in lines:
        nums = line.split()
        left.append(int(nums[0]))
        right.append(int(nums[-1]))
    

    # Part I    

    left.sort()
    right.sort()

    ans1 = 0
    for l,r in zip(left, right):
        ans1 += abs(l-r)

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    cr = Counter(right)

    ans2 = 0

    for l in left:
        ans2 += cr[l]*l
    
    print(f'Answer to part 2: {ans2}')
