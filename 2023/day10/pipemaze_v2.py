""" Advent of Code 2023 -- Day 10 -- """
year = 2023
day = 10     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
import matplotlib.path as mpltPath
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches

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
    polygon = [posS, pos]
    
    while get_tile(pos, lines) != 'S': # and steps <= 20:
        new_pos = find_next(old_pos, pos, lines)
        polygon.append(new_pos)
        old_pos, pos = pos, new_pos
        # print(steps, new_pos, get_tile(new_pos,lines))
        step += 1

    ans1 = step//2 

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    N = len(lines)
    M = len(lines[0])

    path = mpltPath.Path(polygon)

    candidates = []

    for j in range(N):
        for i in range(M):
            if (j,i) in polygon:
                # skip all tiles which are part of the loop
                continue
            candidates.append((j,i))
    enclosed = path.contains_points(candidates)
    ans2 = np.count_nonzero(enclosed)
    
    # to create the plot of the maze
    # fig, ax = plt.subplots()
    # patch = patches.PathPatch(path, facecolor='orange', lw=2)
    # ax.add_patch(patch)
    # ax.set_xlim(-1, M)
    # ax.set_ylim(-1, N)
    # plt.show()
    
    print(f'Answer to part 2: {ans2}')
