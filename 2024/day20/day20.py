""" Advent of Code 2024 -- Day 20 -- """
year = 2024
day = 20     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
from scipy.sparse import csr_array
from scipy.sparse.csgraph import dijkstra, reconstruct_path

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    counter = 0
    coord = dict()
    coord_inv = []
    for k, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != '#':
                coord[(k,j)] = counter
                coord_inv.append((k,j))
                counter += 1

    I = []
    J = []

    for k, l in coord.keys():
        i = coord[(k,l)]

        dirs = {0: (0,1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}

        for d in range(4):
            nb = (k+dirs[d][0], l+dirs[d][1])
            if lines[nb[0]][nb[1]] != '#':
                j = coord[nb]
                I.append(i)
                J.append(j)

    I = np.array(I, dtype=np.int32)
    J = np.array(J, dtype=np.int32)
    data = np.array(len(I)*[1], dtype=int)
    W = csr_array( (data, (I, J)), dtype=int)

    return lines, coord, coord_inv, W


def find_S_E(maze):
    for m, line in enumerate(maze):
        for n, c in enumerate(line):
            if c == 'S':
                S = (m,n)
            if c == 'E':
                E = (m,n)

    return S, E

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    maze, coord, coord_inv, W = parsing(data)
    S, E = find_S_E(maze)
    print('Start:', coord[S])
    print('Goal:', coord[E])
    # print(coord)

    
    dist, pred = dijkstra(W, directed=False, unweighted=True,
                          return_predecessors=True, indices=coord[S])
    lim = dist[coord[E]] - 100
    path = reconstruct_path(W, pred, directed=False)

    dist2, pred2 = dijkstra(W, directed=False, unweighted=True,
                          return_predecessors=True, indices=coord[E])
    print(dist2[coord[S]])

    # Part I    
    N = len(coord)

    ans1 = 0

    for n in range(N):
        for m in range(N):
            pt1 = coord_inv[n]
            pt2 = coord_inv[m]
            d = abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

            if d <= 2 and dist[n] + dist2[m] + d <= lim:
                ans1 += 1


    print(f'Answer to part 1: {ans1}')

    # Part II


    ans2 = 0

    for n in range(N):
        for m in range(N):
            pt1 = coord_inv[n]
            pt2 = coord_inv[m]
            d = abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

            if d <= 20 and dist[n] + dist2[m] + d <= lim:
                ans2 += 1

    print(f'Answer to part 2: {ans2}')
