""" Advent of Code 2024 -- Day 6 -- """
year = 2024
day = 6     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    area = []
    for m, line in enumerate(lines):
        n = line.find('^')
        if n != -1:
            start = (m,n)

        area.append([c for c in line])

    return area, start



if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    lines, pos = parsing(data)

    # Part I    

    dirs = [(-1,0), (0,1), (1, 0), (0, -1)]
    d = 0

    M = len(lines)
    N = len(lines[0])
    # print(M, N)

    lines[pos[0]][pos[1]] = 'X'
    
    cands = set()

    while True:
        new_pos = (pos[0] + dirs[d][0], pos[1] + dirs[d][1])
                
        if new_pos[0] < 0 or new_pos[0] == M or new_pos[1] < 0 or new_pos[1] == N:
            break

        if lines[new_pos[0]][new_pos[1]] == '#':
            d = (d + 1) % 4
            continue
        
        pos = new_pos
        lines[pos[0]][pos[1]] = 'X'
        cands.add(pos)
        
    ans1 = 0
    for line in lines:
        ans1 += line.count('X')
    
    print(f'Answer to part 1: {ans1}')

    # Part II
    

    ans2 = 0

    for j, cand in enumerate(cands):
        lines2, pos = parsing(data)
        start = (pos[0], pos[1])
        
        path = set()
        d = 0
        path.add((start, d))

        lines2[cand[0]][cand[1]] = '#'
        pos = start

        
        while True:
            new_pos = (pos[0] + dirs[d][0], pos[1] + dirs[d][1])
            
            if new_pos[0] < 0 or new_pos[0] == M or new_pos[1] < 0 or new_pos[1] == N:
                break

            if lines2[new_pos[0]][new_pos[1]] == '#':
                d = (d + 1) % 4
                path.add((pos,d))
                continue

            pos = (new_pos[0], new_pos[1])
            if (pos, d) in path:
                ans2 += 1
                break
            else : 
                path.add((pos,d))
    
    print(f'Answer to part 2: {ans2}')
