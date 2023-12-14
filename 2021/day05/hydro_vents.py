""" Advent of Code 2021 05 -- """
year = 2021
day = 5     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    coords = []

    for line in lines:
        coord = []
        cs = line.split(' -> ')

        for c in cs:
            x,y = c.split(',')
            coord.append(int(x))
            coord.append(int(y))
        
        coords.append(coord)

    return np.array(coords)

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    coords = parsing(data)
    
    # Part I    

    M = np.max(coords[:,0])
    N = np.max(coords[:,1])
    
    ocean_floor = np.zeros((M+1,N+1), dtype=int)

    for c in coords:
        if c[0] == c[2]:
            ocean_floor[c[0], min(c[1], c[3]):max(c[1],c[3])+1] += 1
            continue
        if c[1] == c[3]:
            ocean_floor[min(c[0], c[2]):max(c[0],c[2])+1, c[1]] += 1
            continue

    ans1 = np.count_nonzero(ocean_floor >= 2)

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ocean_floor = np.zeros((M+1,N+1), dtype=int)

    for c in coords:
        if c[0] == c[2]:
            ocean_floor[c[0], min(c[1], c[3]):max(c[1],c[3])+1] += 1
            continue
        if c[1] == c[3]:
            ocean_floor[min(c[0], c[2]):max(c[0],c[2])+1, c[1]] += 1
            continue
        if c[0] - c[2] == c[1] - c[3]:
            d = abs(c[2] - c[0])
            for j in range(d+1):
                ocean_floor[min(c[0], c[2])+j, min(c[1], c[3]) + j] += 1
        if c[0] - c[2] == c[3] - c[1]:
            d = abs(c[2] - c[0])
            for j in range(d+1):
                ocean_floor[min(c[0], c[2])+j, max(c[1], c[3]) - j] += 1

    ans2 = np.count_nonzero(ocean_floor >= 2)
    
    print(f'Answer to part 2: {ans2}')
