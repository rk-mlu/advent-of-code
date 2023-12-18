""" Advent of Code 2023 -- Day 18 -- """
year = 2023
day = 18     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
import matplotlib.path as mpltPath
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from itertools import pairwise

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    directions = []

    for line in lines:
        w = line.split()
        if w[0] == 'R':
            d = (1,0)
        if w[0] == 'D':
            d = (0,-1)
        if w[0] == 'U':
            d = (0, 1)
        if w[0] == 'L':
            d = (-1,0)

        steps = int(w[1])

        color = w[2][1:-1]

        directions.append((d, steps, color))

    return directions

def min_max_x(polygon):
    max_x = 0
    min_x = 0
    for vertex in polygon:
        if vertex[0] < min_x:
            min_x = vertex[0]
        if vertex[0] > max_x:
            max_x = vertex[0]
    return (min_x, max_x)

def min_max_y(polygon):
    max_y = 0
    min_y = 0
    for vertex in polygon:
        if vertex[1] < min_y:
            min_y = vertex[1]
        if vertex[1] > max_y:
            max_y = vertex[1]
    return (min_y, max_y)

def hex2direction(instr):
    n = int(instr[1:6], 16)

    if instr[-1] == '0':
        d = (1,0)
    if instr[-1] == '1':
        d = (0,-1)
    if instr[-1] == '2':
        d = (-1,0)
    if instr[-1] == '3':
        d = (0, 1)

    return (d, n)

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    plan = parsing(data)

    # Part I    

    pos = (0,0)
    polygon = [pos]
    ans1 = 0

    for p in plan:
        d = p[0]
        ans1 += p[1]
        # for k in range(p[1]):
        pos = (pos[0] + p[1]*d[0], pos[1] + p[1]*d[1])
        polygon.append(pos)

    x_min, x_max = min_max_x(polygon)
    y_min, y_max = min_max_y(polygon)
    
    path = mpltPath.Path(polygon)

    for i in range(x_min, x_max+1):
        candidates = i*np.ones((2, y_max-y_min+1))
        candidates[1,:] = np.arange(y_min, y_max+1)
        # print(candidates.T)
        enclosed = path.contains_points(candidates.T, radius=0.05)
        ans1 += np.count_nonzero(enclosed)

    print(f'Answer to part 1: {ans1}')

    # to create the plot of the maze
    fig, (ax1, ax2) = plt.subplots(2,1)
    patch = patches.PathPatch(path, facecolor='orange', lw=2)
    ax1.add_patch(patch)
    ax1.set_xlim(x_min-1, x_max+1)
    ax1.set_ylim(y_min-1, y_max+1)
    # plt.show()

    # Part II
    
    instr = []
    for p in plan:
        instr.append(hex2direction(p[2]))
    
    
    pos1 = (0,0)
    polygon1 = [pos1]

    for p in instr:
        d = p[0]
        # for k in range(p[1]):
        pos_x1 = pos1[0] + p[1]*d[0]
        pos_y1 = pos1[1] + p[1]*d[1]
        pos1 = (pos_x1, pos_y1)
        polygon1.append(pos1)

    path1 = mpltPath.Path(polygon1)
    
    polygon2 = []
    set_x2 = set()
    set_y2 = set()
    for v in polygon1:
        dirs = [(1,1), (1,-1), (-1, 1), (-1,-1)]
        num_vert = 0
        for d in dirs:
            cand = (v[0]+0.49999999*d[0], v[1]+0.49999999*d[1])
            if path1.contains_point(cand, radius=0.01):
                num_vert += 1
       
        if num_vert == 1:
            for d in dirs:
                cand = (v[0]+0.499999999*d[0], v[1]+0.49999999*d[1])
                if path1.contains_point(cand, radius=0.01):
                    pos_x2 = v[0] - 0.499999999*d[0]
                    set_x2.add(pos_x2)
                    pos_y2 = v[1] - 0.499999999*d[1]
                    set_y2.add(pos_y2)
                    pos2 = (pos_x2, pos_y2)
                    polygon2.append(pos2)
        else: 
            for d in dirs:
                cand = (v[0]+0.499999999*d[0], v[1]+0.499999999*d[1])
                if not path1.contains_point(cand, radius=0.01):
                    pos_x2 = v[0] + 0.499999999*d[0]
                    set_x2.add(pos_x2)
                    pos_y2 = v[1] + 0.499999999*d[1]
                    set_y2.add(pos_y2)
                    pos2 = (pos_x2, pos_y2)
                    polygon2.append(pos2)

    x_min1, x_max1 = min_max_x(polygon2)
    y_min1, y_max1 = min_max_y(polygon2)

    vert_x1 = list(set_x2)
    vert_x1.sort()
    vert_y1 = list(set_y2)
    vert_y1.sort()
    path2 = mpltPath.Path(polygon2)

    ans2 = 0

    for (x1, x2) in pairwise(vert_x1):
        for (y1, y2) in pairwise(vert_y1):
            if path2.contains_point((x1+0.1, y1+0.1), radius=0.01):
                area = (x2-x1)*(y2-y1)
                ans2 += area

    # to create the plot of the maze
    patch = patches.PathPatch(path2, facecolor='orange', lw=2)
    ax2.add_patch(patch)
    ax2.set_xlim(x_min1-1, x_max1+1)
    ax2.set_ylim(y_min1-1, y_max1+1)
    plt.show()
    
    print(f'Answer to part 2: {round(ans2)}')
