""" Advent of Code 2024 -- Day 05 -- """
year = 2024
day = 5     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np
from itertools import pairwise, combinations
from collections import Counter

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    ordering = set()
    updates = []
    for line in lines:
        if '|' in line:
            ordering.add(line)
        elif len(line)>0:
            up = line.split(',')
            updates.append(up)

    return ordering, updates

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    ordering, updates = parsing(data)

    # Part I    

    ans1 = 0

    for up in updates:
        in_order = True
        for p1, p2 in pairwise(up):
            s = p1 + '|' + p2
            if s not in ordering:
                in_order = False
                break
        if in_order:
            n = len(up)
            ans1 += int(up[n//2])
    
    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    
    for up in updates:
        in_order = True
        
        list_maxi = Counter(up)

        for p1, p2 in combinations(up, 2):
            s = p1 + '|' + p2
            if s in ordering:
                list_maxi[p2] += 1
                continue
            
            s = p2 + '|' + p1
            if  s in ordering:
                in_order = False
                list_maxi[p1] += 1
            else :
                print(f'pair {p1} and {p2} not found.')
                

        if not in_order:
            ordered = list_maxi.most_common()
            
            n = len(up)
            ans2 += int(ordered[n//2][0])
    
    print(f'Answer to part 2: {ans2}')
