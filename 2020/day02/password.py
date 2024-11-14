""" Advent of Code 2020 -- Day 02 -- """
year = 2020
day = 2     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np
from collections import Counter

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    return lines

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    lines = parsing(data)
    
    policies = []
    for line in lines:
        ran, letter, pw = line.split()
        low, up = ran.split('-')
        letter = letter[0]

        policies.append((int(low), int(up), letter, pw))

    # Part I    
    
    valid = 0
    for pol in policies:
        c = Counter(pol[-1])
        num_letter = c.get(pol[2], 0)
        if (num_letter >= pol[0]) and (num_letter <= pol[1]):
            valid += 1

    ans1 = valid

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    valid = 0
    for pol in policies:
        pw = pol[-1]
        pos1 = pol[0] - 1
        pos2 = pol[1] - 1
        if (pw[pos1] == pol[2]) ^ (pw[pos2] == pol[2]):
            valid += 1
    
    ans2 = valid
    
    print(f'Answer to part 2: {ans2}')
