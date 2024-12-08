""" Advent of Code 2024 -- Day 8 -- """
year = 2024
day = 8     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np
from itertools import combinations

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    antennas = dict()

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '.':
                continue
            pos = antennas.setdefault(c, [])
            pos.append((i,j))

    return lines, antennas

def test_inside(i,j,M,N):
    return not(i < 0 or j < 0 or i >= M or j >= N)

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    lines, antennas = parsing(data)

    M = len(lines)
    N = len(lines[0])

    # Part I    


    antinodes = set()

    for freq, pos in antennas.items():
        for p1, p2 in combinations(pos, 2):
            d0 = p2[0] - p1[0]
            d1 = p2[1] - p1[1]
            cand1 = (p1[0] - d0, p1[1] - d1)
            if test_inside(cand1[0], cand1[1], M, N):
                antinodes.add(cand1)
            cand2 = (p2[0] + d0, p2[1] + d1)
            if test_inside(cand2[0], cand2[1], M, N):
                antinodes.add(cand2)


    ans1 = len(antinodes)

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    antinodes2 = set()

    for freq, pos in antennas.items():
        if len(pos) <= 1:
            continue
        else:
            for p in pos:
                antinodes2.add(p)
            for p1, p2 in combinations(pos, 2):
                d0 = p2[0] - p1[0]
                d1 = p2[1] - p1[1]
                cand1 = (p1[0] - d0, p1[1] - d1)
                while test_inside(cand1[0], cand1[1], M, N):
                    antinodes2.add(cand1)
                    cand1 = (cand1[0] - d0, cand1[1] - d1)

                cand2 = (p2[0] + d0, p2[1] + d1)
                while test_inside(cand2[0], cand2[1], M, N):
                    antinodes2.add(cand2)
                    cand2 = (cand2[0] + d0, cand2[1] + d1)


    ans2 = len(antinodes2)
    
    print(f'Answer to part 2: {ans2}')
