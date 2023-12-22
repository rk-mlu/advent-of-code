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
    # print(np.count_nonzero(garden))
    
    return pos, garden

def get_nb(pos_set, garden):
    M, N = garden.shape
    
    nbs = set()

    while len(pos_set) > 0:
        p = pos_set.pop()
        
        for d in [(0,1), (0,-1), (1,0), (-1,0)]:
            cand = (p[0] + d[0], p[1] + d[1])
            if garden[cand] == 1:
                nbs.add(cand)

    return nbs

def get_nb2(pos_set, garden):
    M, N = garden.shape
    
    nbs = set()

    while len(pos_set) > 0:
        p = pos_set.pop()
        
        for d in [(0,1), (0,-1), (1,0), (-1,0)]:
            
            c0 = p[0] + d[0]
            c1 = p[1] + d[1]
            c2 = p[2]
            c3 = p[3]

            if c0 == -1:
                c0 = M-1
                c2 -= 1
            if c0 == M:
                c0 = 0
                c2 += 1
            if c1 == -1:
                c1 = N-1
                c3 -= 1
            if c1 == N:
                c1 = 0
                c3 += 1

            cand = (c0, c1, c2, c3)

            if garden[(cand[0],cand[1])] == 1:
                nbs.add(cand)

    return nbs

def part1(start_pos, steps):
    reachable = {start_pos}

    for j in range(steps):
        reachable = get_nb(reachable, garden) 

    return len(reachable)



if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    pos1, garden = parsing(data)

    M, N = garden.shape

    # Part I    
    
    steps = 64

    ans1 = part1(pos1, steps)

    print(f'Answer to part 1: {ans1}')
    

    # Part II
    
    steps = 26501365 - 65
    multiple = steps // 131 

    odd = part1((66,66), 131)
    even = part1((66,66),132)
    
    # center
    ans2 = odd 
    
    # fully filled neighboring tiles (2 periodic odd and even)
    ans2 += (multiple-2)*(multiple)*odd + (multiple)**2*even

    # boundary corners
    ans2 += part1((66,1), 130) + part1((1,66), 130) + part1((131,66), 130)
    ans2 += part1((66,131), 130)
    
    # diagonal boundary
    d1 = multiple * part1( (1,1), 64) + (multiple - 1)*part1( (1,1), 64+131)
    d2 = multiple * part1( (131,131), 64) + (multiple - 1)* part1( (131,131), 64+131)
    d3 = multiple * part1( (131,1), 64) + (multiple - 1)*part1( (131,1), 64+131)
    d4 = multiple * part1( (1,131), 64) + (multiple - 1)*part1( (1,131), 64+131)
    
    ans2 += d1 + d2 + d3 + d4
    
    print(f'Answer to part 2: {ans2}')
