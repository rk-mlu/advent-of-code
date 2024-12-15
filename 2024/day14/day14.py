""" Advent of Code 2024 -- Day 14 -- """
year = 2024
day = 14     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
import matplotlib.pyplot as plt

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    robots = []
    
    for line in lines:
        words = line.split()
        p1, p2 = words[0][2:].split(',')
        v1, v2 = words[1][2:].split(',')
        robots.append((int(p1), int(p2), int(v1), int(v2)))

    return robots

def get_image(seconds, robots):
    M, N = 101, 103

    tiles = np.zeros((M,N), dtype=int)

    for r in robots:
        p0, p1 = r[0], r[1]
        p0 = (p0 + seconds*r[2]) % M
        p1 = (p1 + seconds*r[3]) % N
        
        tiles[p0,p1] += 1

    return tiles.T

def get_components(tiles):
    M, N = tiles.shape
    
    visited = dict()
    components = []

    for x in range(M):
        for y in range(N):
            if tiles[x, y]:
                v = (x,y)
                vis = visited.get(v, False)

                if vis:
                    continue
                else :
                    comp = DFS(v, tiles, visited)

                components.append(comp)

    return len(components)

def get_nbs(v, tiles):
    M, N = tiles.shape
    dirs = [(1,0), (0,1), (-1, 0), (0,-1)]

    nbs = []

    for d in dirs:
        cand0 = (v[0] + d[0]) % M
        cand1 = (v[1] + d[1]) % N

        if tiles[cand0, cand1] > 0:
            nbs.append((cand0, cand1))

    return nbs

def DFS(v, tiles, visited):
    comp = set()
    comp.add(v)
    visited[v] = True

    nbs = get_nbs(v, tiles)

    for nb in nbs:
        if not(visited.get(nb, False)):
            comp2 = DFS(nb, tiles, visited)
            comp.update(comp2)

    return comp

    
if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    robots = parsing(data)

    # Part I    
    
    M, N = 101, 103
    # M, N = 11, 7

    seconds = 100

    tiles = np.zeros( (M,N), dtype=int)

    for r in robots:
        p0, p1 = r[0], r[1]
        p0 = (p0 + seconds*r[2]) % M
        p1 = (p1 + seconds*r[3]) % N
        
        tiles[p0,p1] += 1
    
    q1 = np.sum(tiles[:M//2,:N//2])
    q2 = np.sum(tiles[M//2+1:,:N//2])
    q3 = np.sum(tiles[:M//2,N//2+1:])
    q4 = np.sum(tiles[M//2+1:,N//2+1:])

    ans1 = q1*q2*q3*q4

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    frames = 10000

    num_comps = []
    
    for j in range(frames):
        tiles = get_image(j, robots)
        
        k = get_components(tiles)
        num_comps.append((k,j))
    
    # sort to find configuration with smalles number of components
    num_comps.sort()

    # plot a few candidates
    num_cands = 1
    for k, j in num_comps[:num_cands]:
        fig, ax = plt.subplots()
        im = ax.imshow(get_image(j, robots))
        ax.set_title(f'frame {j}, num comps: {k}')

    plt.savefig('christmas_tree.png')
    plt.show()
    
    ans2 = [j for (k, j) in num_comps[:num_cands]]
    
    print(f'Answer to part 2: {ans2}')
