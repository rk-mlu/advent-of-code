""" Advent of Code 2023 -- Day 10 -- """
year = 2023
day = 10     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    return lines

def get_tile(pos, lines):
    N = len(lines)
    M = len(lines[0])
    if pos[0] == -1 or pos[0] == N:
        return '.'
    if pos[1] == -1 or pos[1] == M:
        return '.'
    return lines[pos[0]][pos[1]]

def first_step(posS, lines):
    above = (posS[0]-1, posS[1])
    t = get_tile(above, lines)
    if t in {'|', '7', 'F'}:
        return above
    left = (posS[0], posS[1]-1)
    t = get_tile(left, lines)
    if t in {'-', 'L', 'F'}:
        return left
    below = (posS[0]+1, posS[1])
    t = get_tile(below, lines)
    if t in {'|', 'L', 'J'}:
        return below

def find_next(old_pos, pos, lines):
    pipe = get_tile(pos, lines)

    if pipe == '|':
        pos1 = (pos[0]+1,pos[1])
        pos2 = (pos[0]-1,pos[1])
        if old_pos[0] == pos1[0]:
            return pos2
        else :
            return pos1

    if pipe == '-':
        pos1 = (pos[0],pos[1]+1)
        pos2 = (pos[0],pos[1]-1)
        if old_pos[1] == pos1[1]:
            return pos2
        else :
            return pos1
    
    if pipe == 'L':
        pos1 = (pos[0],pos[1]+1)
        pos2 = (pos[0]-1,pos[1])
        if old_pos[0] == pos1[0] and old_pos[1] == pos1[1]:
            return pos2
        else :
            return pos1

    if pipe == 'J':
        pos1 = (pos[0],pos[1]-1)
        pos2 = (pos[0]-1,pos[1])
        if old_pos[0] == pos1[0] and old_pos[1] == pos1[1]:
            return pos2
        else :
            return pos1
    
    if pipe == '7':
        pos1 = (pos[0],pos[1]-1)
        pos2 = (pos[0]+1,pos[1])
        if old_pos[0] == pos1[0] and old_pos[1] == pos1[1]:
            return pos2
        else :
            return pos1
    
    if pipe == 'F':
        pos1 = (pos[0],pos[1]+1)
        pos2 = (pos[0]+1,pos[1])
        if old_pos[0] == pos1[0] and old_pos[1] == pos1[1]:
            return pos2
        else :
            return pos1

def find_next2(old_pos, pos, lines):
    pipe = get_tile(pos, lines)

    if pipe == '|':
        pos1 = (pos[0]+1,pos[1])
        pos2 = (pos[0]-1,pos[1])
        if old_pos[0] == pos1[0]:
            return pos2, (-1,0)
        else :
            return pos1, (1, 0)

    if pipe == '-':
        pos1 = (pos[0],pos[1]+1)
        pos2 = (pos[0],pos[1]-1)
        if old_pos[1] == pos1[1]:
            return pos2, (0, -1)
        else :
            return pos1, (0, 1)

    if pipe == 'L':
        pos1 = (pos[0],pos[1]+1)
        pos2 = (pos[0]-1,pos[1])
        if old_pos[0] == pos1[0] and old_pos[1] == pos1[1]:
            return pos2, (-1,-1)
        else :
            return pos1, (1, 1)

    if pipe == 'J':
        pos1 = (pos[0],pos[1]-1)
        pos2 = (pos[0]-1,pos[1])
        if old_pos[0] == pos1[0] and old_pos[1] == pos1[1]:
            return pos2, (-1, 1)
        else :
            return pos1, (1, -1)
    
    if pipe == '7':
        pos1 = (pos[0],pos[1]-1)
        pos2 = (pos[0]+1,pos[1])
        if old_pos[0] == pos1[0] and old_pos[1] == pos1[1]:
            return pos2, (1,1)
        else :
            return pos1, (-1, -1)
    
    if pipe == 'F':
        pos1 = (pos[0],pos[1]+1)
        pos2 = (pos[0]+1,pos[1])
        if old_pos[0] == pos1[0] and old_pos[1] == pos1[1]:
            return pos2, (1, -1)
        else :
            return pos1, (-1, 1)


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    lines = parsing(data)

    # Part I    
    
    for j, line in enumerate(lines):
        k = line.find('S')
        if k != -1:
            posS = (j,k)
    
    old_pos = posS
    pos = first_step(posS, lines)
    # print(old_pos, pos)
    
    step = 1
    
    while get_tile(pos, lines) != 'S': # and steps <= 20:
        new_pos = find_next(old_pos, pos, lines)
        old_pos, pos = pos, new_pos
        # print(steps, new_pos, get_tile(new_pos,lines))
        step += 1

    ans1 = step//2 

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    N = len(lines)
    M = len(lines[0])

    enclosed = 2*np.ones((N,M), dtype=int)
    # tiles = np.zeros((N,M), dtype=int)
    
    old_pos = posS
    pos = first_step(posS, lines)

    enclosed[old_pos] = 3   # mark loop tiles with 3
    enclosed[pos] = 3

    loop2orient = dict()

    t = get_tile(pos, lines)
    while t != 'S':
        new_pos, orient = find_next2(old_pos, pos, lines)
        loop2orient[pos] = orient
        old_pos, pos = pos, new_pos
        t = get_tile(pos, lines)
        enclosed[pos] = 3

    for j in range(N):
        for i in range(M):
            if enclosed[j,i] == 3:
                # skip all tiles which are part of the loop
                continue

            if j == 0 or j==N-1 or i == 0 or i == M-1:
                # boundary is outside
                enclosed[j,i] = 0
                continue

            if enclosed[j, i-1] == 0 or enclosed[j-1, i] == 0:
                # if neighbor is outside, so is this tile
                enclosed[j,i] = 0
                continue

            if enclosed[j, i-1] == 1 or enclosed[j-1, i] == 1:
                # if neighbor is enclosed, so is this tile
                enclosed[j,i] = 1
                continue
            
            # new candidate for an enclosed tile
            # Check orientation of flow in loop in the tile above
            orient = loop2orient[(j-1,i)]
            if orient[1] < 0:
                # flow right to left means tile is outside
                enclosed[j,i] = 0
            else :
                # flow left to right means tile is enclosde
                enclosed[j,i] = 1

    ans2 = np.count_nonzero(enclosed==1)
    
    print(f'Answer to part 2: {ans2}')
