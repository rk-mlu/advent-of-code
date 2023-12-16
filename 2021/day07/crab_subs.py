""" Advent of Code 2021 -- Day 07 -- """
year = 2021
day = 7     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
from collections import Counter
from itertools import product

def parsing(data):
    # parser for the input data    
    sub_pos = [int(n) for n in data.split(',')]

    return sub_pos

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    sub_pos = parsing(data)
    
    c = Counter(sub_pos)
    
    pos = list(c.keys())
    pos.sort()

    # Part I    
    mini = pos[0]
    maxi = pos[-1]

    fuel = np.zeros(maxi-mini+1, dtype=int)
    for (i,p) in product(range(mini,maxi+1),pos):
        fuel[i] += c[p]*abs(p-i)
    
    ans1  = np.min(fuel)            

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    fuel = np.zeros(maxi-mini+1, dtype=int)
    for (i,p) in product(range(mini,maxi+1),pos):
        d = abs(p-i)
        fuel[i] += c[p]*abs(d*(d+1)//2)
    
    ans2  = np.min(fuel)            
    
    print(f'Answer to part 2: {ans2}')
