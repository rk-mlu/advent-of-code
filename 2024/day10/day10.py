""" Advent of Code 2024 -- Day 10 -- """
year = 2024
day = 10     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np
import heapq

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    M = len(lines)
    N = len(lines[0])

    out = []
    s = '.'*(N+2)
    out.append(s)
    for line in lines:
        s = '.'
        s += line
        s += '.'
        out.append(s)
    out.append('.'*(N+2))

    return out

def explore(start, lines):
    queue = [start]
    heapq.heapify(queue)
    
    visited = set()
    nines = set()
    
    dirs = [(-1,0), (0, 1), (1, 0), (0, -1)] 

    while len(queue) > 0:
        cur = heapq.heappop(queue)
        if cur in visited:
            continue
        else :
            visited.add(cur)

            for d in dirs:
                i = cur[1] + d[0]
                j = cur[2] + d[1]
                v = lines[i][j]
                if v == '.':
                    continue
                if int(v) == int(cur[0]) + 1:
                    if int(v) == 9:
                        nines.add((i,j))
                    else :
                        heapq.heappush(queue, (v,i,j))

    return len(nines)

def explore2(start, lines):
    
    dirs = [(-1,0), (0, 1), (1, 0), (0, -1)] 
    out = 0

    if start[0] == '9':
        return 1

    for d in dirs:
        i = start[1] + d[0]
        j = start[2] + d[1]
        v = lines[i][j]
        if v == '.':
            continue
        if int(v) == int(start[0]) + 1:
            out += explore2((v,i,j), lines)

    return out


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    lines = parsing(data)

    # Part I    
    print(lines)
    starts = []

    for m, line in enumerate(lines):
        for n, c in enumerate(line):
            if c == '0':
                starts.append((0,m,n))

    ans1 = 0

    for start in starts:
        ans1 += explore(start, lines)

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    for start in starts:
        ans2 += explore2(start, lines)
    
    print(f'Answer to part 2: {ans2}')
