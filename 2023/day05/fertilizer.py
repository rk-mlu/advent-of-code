""" Advent of Code 2023 -- Day 05 -- """

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

def new_map(x, table):
    for cond in table:
        if x >= cond[1] and x < cond[1]+cond[2]:
            return cond[0] + x - cond[1]
    return x

if __name__ == '__main__':
    data = aoc.get_input('input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    lines = data.splitlines()

    # Part I    
    seeds, tables = parse_data(lines)
    print(tables)
    locations = []

    for seed in seeds:
        x = seed
        for tab in tables:
            x = new_map(x, tab)
        locations.append(x)

    ans1 = min(locations)

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    
    print(f'Answer to part 2: {ans2}')
