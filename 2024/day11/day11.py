""" Advent of Code 2024 -- Day 11 -- """
year = 2024
day = 11     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np
from math import log10, ceil
from collections import Counter

def parsing(data):
    # parser for the input data    
    # lines = data.splitlines()
    stones = [int(n) for n in data.split()]
        
    return stones

def blink(stones):
    new_stones = []

    for s in stones:
        if s == 0:
            new_stones.append(1)
            continue

        e = ceil(log10(s+1))
        if e % 2 == 0:
            s1, s2 = divmod(s, 10**(e/2))
            new_stones.append(int(s1))
            new_stones.append(int(s2))
            continue

        new_stones.append(2024*s)

    return tuple(new_stones)

def blink3(s):
    new_stones = (s,)
    for j in range(3):
        new_stones = blink(new_stones)
    return new_stones


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    stones = parsing(data)


    # Part I    

    # print(stones)
    lens = []
    
    num_iter = 25

    for i in range(num_iter):
        stones = blink(stones)
        lens.append(len(stones))

    ans1 = len(stones)

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    num_iter2 = 75
    stones = parsing(data)
    cnt = Counter(stones)

    
    for i in range(num_iter2): 

        cnt_new = Counter()
        for (s, n) in cnt.items():
            new_stones = blink([s])
            c_temp = Counter(new_stones)
            for (s1, n1) in c_temp.items():
                cnt_new[s1] += n*n1
        cnt = cnt_new
            
    ans2 = cnt.total()
        


    print(f'Answer to part 2: {ans2}')
