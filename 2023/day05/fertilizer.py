""" Advent of Code 2023 -- Day 05 --
Run time: about 10 s with my input data
"""

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parse_data(lines):
    seeds = lines[0].split(':')
    seeds = [int(s) for s in seeds[1].split()]

    tables = []
    tab_counter = -1

    for line in lines[1:]:
        if len(line)== 0:
            continue
        if line.endswith('map:'):
            # found new map definition
            tab_counter += 1
            tables.append([])
            continue
        dest, sour, ran = line.split()
        tables[tab_counter].append((int(dest), int(sour), int(ran))) 

    return seeds, tables

def seed2loc(s, tables):
    l = s
    
    for tab in tables:
        for cond in tab:
            if l >= cond[1] and l < cond[1]+cond[2]:
                l = cond[0] + l - cond[1]
                break

    return l

def loc2seed(l, tables):
    # inverse of seed2loc 
    m = len(tables)

    s = l
    for j in range(m):
        for cond in tables[m-j-1]:
            if s >= cond[0] and s < cond[0]+cond[2]:
                s = cond[1] + s - cond[0]
                break
    return s

def admissible(s, seeds):
    m = len(seeds)//2

    for j in range(m):
        if s >= seeds[2*j] and s < seeds[2*j] + seeds[2*j+1]:
            return True
    return False

if __name__ == '__main__':
    data = aoc.get_input('input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    lines = data.splitlines()

    # Part I    
    seeds, tables = parse_data(lines)
    locations = []

    for seed in seeds:
        locations.append(seed2loc(seed, tables))

    ans1 = min(locations)

    print(f'Answer to part 1: {ans1}')

    # Part II
    print("Computing solutions to part II...(takes a few seconds)")
    l = 0
    s = loc2seed(l, tables)
    while not admissible(s, seeds):
        l += 1
        s = loc2seed(l, tables)
    ans2 = l
    
    print(f'Answer to part 2: {ans2}')
