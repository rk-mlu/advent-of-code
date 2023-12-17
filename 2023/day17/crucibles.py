""" Advent of Code 2023 -- Day 17 -- """
year = 2023
day = 17     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
from itertools import product

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    M = len(lines)
    N = len(lines[0])

    blocks = np.zeros( (M,N), dtype = int)

    for i in range(M):
        for j in range(N):
            blocks[i,j] = int(lines[i][j])

    return blocks

def get_neighbors(vertex, M,N,part):
    neighbors = []

    if part == 1:
        if vertex[2] == 'h' or vertex[2] is None:
            for i in range(3):
                vd = (vertex[0] + i + 1, vertex[1], 'v')
                vu = (vertex[0] - i - 1, vertex[1], 'v')
                if vd[0] < M:
                    neighbors.append(vd)
                if vu[0] >= 0:
                    neighbors.append(vu)
        if vertex[2] == 'v' or vertex[2] is None:
            for i in range(3):
                vr = (vertex[0], vertex[1] + i + 1, 'h')
                vl = (vertex[0], vertex[1] - i - 1, 'h')
                if vr[1] < N:
                    neighbors.append(vr)
                if vl[1] >= 0:
                    neighbors.append(vl)

    if part == 2:
        if vertex[2] == 'h' or vertex[2] is None:
            for i in range(3,10):
                vd = (vertex[0] + i + 1, vertex[1], 'v')
                vu = (vertex[0] - i - 1, vertex[1], 'v')
                if vd[0] < M:
                    neighbors.append(vd)
                if vu[0] >= 0:
                    neighbors.append(vu)
        if vertex[2] == 'v' or vertex[2] is None:
            for i in range(3,10):
                vr = (vertex[0], vertex[1] + i + 1, 'h')
                vl = (vertex[0], vertex[1] - i - 1, 'h')
                if vr[1] < N:
                    neighbors.append(vr)
                if vl[1] >= 0:
                    neighbors.append(vl)

    return neighbors


def part(a, blocks):
    
    M,N = blocks.shape

    # initialize graph
    dist = dict()
    prev = dict()
    vertices = []
    # initial position
    dist[(0,0,None)] = 0
    prev[(0,0,None)] = None
    vertices.append((0,0,None))

    # all other vertices
    for i, j, d in product(range(M), range(N), ['h','v']):
        dist[(i,j,d)] = np.inf
        prev[(i,j,d)] = None
        vertices.append((i,j,d))
    
    def dist_v(vertex):
        return dist[vertex]
    

    def get_dist(u,v):
        dist = 0
        if u[0] == v[0]:
            d = v[1] - u[1]
            if d < 0:
                for j in range(-d):
                    dist += blocks[v[0], v[1] + j]
            else :
                for j in range(d):
                    dist += blocks[u[0], u[1] + j + 1]

        if u[0] != v[0]:
            d = v[0] - u[0]
            if d < 0:
                for j in range(-d):
                    dist += blocks[v[0] + j, v[1]]
            else :
                for j in range(d):
                    dist += blocks[u[0] + 1 + j, u[1]]
        return dist

    while len(vertices) > 0:
        vertices.sort(reverse=True, key=dist_v)
        u = vertices.pop() 
        dist_u = dist[u]
        if u[0] == M-1 and u[1] == N-1:
            break

        nbs = get_neighbors(u, M, N, a)
        for nb in nbs:
            if nb in vertices:
                alt_dist = dist_u + get_dist(u, nb)
                if alt_dist < dist[nb]:
                    dist[nb] = alt_dist
                    prev[nb] = u
            # print(nb, dist[nb], prev[nb])
    
    return dist_u

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    blocks = parsing(data)

    # Part I    
    print('Computing shortest path for part 1. This can take several minutes...')
    
    ans1 = part(1, blocks)
    print(f'Answer to part 1: {ans1}')

    # Part II
    print('Computing shortest path for part 2. This can take several minutes...')
    
    ans2 = part(2, blocks)
    
    print(f'Answer to part 2: {ans2}')
