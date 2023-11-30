""" Advent of Code 2022 -- Day 11 -- """

import aoc
import numpy as np
import copy

def parsing(data):
    hmap = np.zeros((41,101), dtype=int)

    for j, line in enumerate(data.splitlines()):
        for m, c in enumerate(line):
            if c == 'S':
                S = (j, m)
                hmap[j,m] = 0
                continue
            if c == 'E':
                E = (j,m)
                hmap[j,m] = 25
                continue
            hmap[j,m] = ord(c) - 97
    return S, E, hmap

def find_path(coord, hmap, uncov):
    
    directions = set()
    row, col = hmap.shape
    j, m = coord[0], coord[1]

    if j + 1 < row:
        d = (j+1, m)
        if hmap[d] - hmap[j,m] <= 1 and not(d in uncov):
            directions.add(d)

    if j - 1 >= 0:
        d = (j-1, m)
        if hmap[d] - hmap[j,m] <= 1 and not(d in uncov):
            directions.add(d)

    if m - 1 >= 0:
        d = (j, m-1)
        if hmap[d] - hmap[j,m] <= 1 and not(d in uncov):
            directions.add(d)

    if m + 1 < col:
        d = (j, m+1)
        if hmap[d] - hmap[j,m] <= 1 and not(d in uncov):
            directions.add(d)
    
    return directions

def shortes_path(S, E, hmap):
    uncovered = set()
    uncovered.add(S)
    dist = [ uncovered.copy()]
    coords_old = set()
    coords_old.add(S)
    
    step = 0
    slim = 1000
    while E not in uncovered and step < slim:

        coords_new = set()
        for d in coords_old:
            dirs = find_path(d, hmap, uncovered)
            for dd in dirs:
                coords_new.add(dd)
                uncovered.add(dd)
        
        dist.append(copy.deepcopy(coords_new))
        coords_old = coords_new
        step += 1

    return step


if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    # Part I
    S, E, hmap = parsing(data)
    steps = shortes_path(S, E, hmap)
    print(f'Part I: Shortest path from {S} to {E} has {steps} steps.')

    # Part II
    mini = 361
    row, col = hmap.shape
    for j in range(row):
        for m in range(col):
            if hmap[j,m] == 0:
                S_new = (j,m)
                
                mini = min(mini, shortes_path(S_new, E, hmap))

    print(f'Part II: Shortest path from any location has {mini} steps.')
