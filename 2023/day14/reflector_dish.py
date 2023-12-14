""" Advent of Code 2023 -- Day 14 -- """
year = 2023
day = 14     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    N = len(lines)
    M = len(lines[0])

    rocks = np.zeros((N,M), dtype=int)

    for i, line in enumerate(lines):
        for j, r in enumerate(line):
            if r == 'O':
                rocks[i,j] = 1
            if r == '#':
                rocks[i,j] = -1
    
    return rocks

def tilt_north(rocks):
    M, N = rocks.shape
    rocks_tilted = rocks.copy()

    for i in range(1,M):
        for j in range(N):
            if rocks_tilted[i,j] == 1:
                for k in range(1,i+1):
                    if rocks_tilted[i-k, j] != 0:
                        break
                    if rocks_tilted[i-k, j] == 0:
                        rocks_tilted[i-k, j] = 1
                        rocks_tilted[i-k+1,j] = 0
    return rocks_tilted

def comp_load(rocks):
    M,N = rocks.shape

    load = 0
    for i in range(M):
        n = np.count_nonzero(rocks[i,:] == 1)
        load += n*(M-i)

    return load

def cycle(rocks):
    rocks_n = tilt_north(rocks)
    
    for j in range(3):
        rocks_rot = np.rot90(rocks_n, k=-1)
        rocks_n = tilt_north(rocks_rot)
    res = np.rot90(rocks_n, k=-1)
    # print(res)
    return res


if __name__ == '__main__':
    # data = aoc.dl_data(day, year, 'input1.txt')                                  
    data = aoc.get_input('input2.txt')
    
    rocks = parsing(data)

    # Part I    

    rocks_n = tilt_north(rocks)
    ans1 = comp_load(rocks_n)

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    warm_up = 100
    rocks_tilt = cycle(rocks)
    
    for j in range(warm_up-1):
        rocks_tilt = cycle(rocks_tilt)
    
    lookup_tab = dict()
    num_samples = 10000
    
    loads = np.zeros(num_samples, dtype=int)
    
    for j in range(num_samples):
        s = rocks_tilt.tobytes()
        if s in lookup_tab.keys():
            rocks_tilt = lookup_tab[s]
        else :
            rocks_tilt = cycle(rocks_tilt)
            lookup_tab[s] = rocks_tilt.copy()
        loads[j] = comp_load(rocks_tilt)
    
    period = len(lookup_tab)
    
    total_cycles = 10**9 - warm_up - 1
    num_cycles = total_cycles // period
    remainder = total_cycles % period 


    ans2 = loads[remainder]

    print(f'Answer to part 2: {ans2}')
