""" Advent of Code 2023 -- Day 21 -- """
year = 2023
day = 21     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    M = len(lines)
    N = len(lines[0])

    garden = np.zeros((M+2,N+2), dtype=int)

    for i, line in enumerate(lines):
        for j in range(N):
            if line[j] in ['.','S']:
                garden[i+1,j+1] = 1
            if line[j] == 'S':
                pos = (i+1,j+1)
    
    return pos, garden

def get_nb(pos_set, garden, look_up_table=dict()):
    M, N = garden.shape
    
    nbs = set()

    while len(pos_set) > 0:
        p = pos_set.pop()

        if p in look_up_table.keys():
            nbs = look_up_table[p]
        
        for d in [(0,1), (0,-1), (1,0), (-1,0)]:
            cand = (p[0] + d[0], p[1] + d[1])
            if garden[cand] == 1:
                nbs.add(cand)

    return nbs

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    pos, garden = parsing(data)

    M, N = garden.shape
    print(M,N, pos)

    # Part I    
    
    reachable = {pos}
    
    look_up_tab = dict()


    steps = 26501365
    for j in range(steps):
        reachable = get_nb(reachable, garden) 
        # print(j+1,reachable)

    ans1 = len(reachable)

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    
    print(f'Answer to part 2: {ans2}')
