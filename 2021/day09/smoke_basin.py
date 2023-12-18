""" Advent of Code 2021 -- Day 09 -- """
year = 2021
day = 9     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    M = len(lines)
    N = len(lines[0])

    heights = 10*np.ones((M+2, N+2), dtype=int)

    for i, line in enumerate(lines):
        for j, n in enumerate(line):
            heights[i+1,j+1] = int(n)

    return heights

def test_low_pt(i,j,height):
    ans = True
    
    for d in [(0,1), (0,-1), (1,0), (-1,0)]:
        if height[i,j] >= height[i+d[0], j+d[1]]:
            ans = False

    return ans

def get_basin(lpt, height):
    basin = {lpt}
    Q = [lpt]

    while len(Q) > 0:
        p = Q.pop()
        for d in [(0,1), (0,-1), (1,0), (-1,0)]:
            nb = (p[0] + d[0], p[1] + d[1])
            if height[nb] < 9 and height[nb] > height[p]:
                Q.append(nb)
                basin.add(nb)

    return basin


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    heights = parsing(data)
    print(heights)

    # Part I    

    M, N = heights.shape

    ans1 = 0

    low_pts = set()
    
    for i in range(1,M-1):
        for j in range(1, N-1):
            if test_low_pt(i, j, heights):
                low_pts.add((i,j))
                ans1 += heights[i,j] + 1

    print(f'Answer to part 1: {ans1}')

    # Part II

    basins = []

    for lpt in low_pts:
        basin = get_basin(lpt, heights)
        basins.append(len(basin))
   
    basins.sort()
    
    ans2 = basins[-1]*basins[-2]*basins[-3]
    
    print(f'Answer to part 2: {ans2}')
