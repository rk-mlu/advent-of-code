""" Advent of Code 2025 -- Day 8 -- """
year = 2025
day = 8         # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
from itertools import combinations
import heapq

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    coords = []

    for line in lines:
        coord = tuple(int(c) for c in line.split(','))
        coords.append(coord)

    return coords

class DSU:
    # union-find data structure 
    def __init__(self, n):
        self.parent = np.arange(n)
        self.n = n
        self.rank = np.zeros(n, dtype=int)
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.components -= 1
        return True

    def extract_components(self):
        groups = {}

        for i in range(self.n):
            root = self.find(i)
            groups.setdefault(root, []).append(i)

        return list(groups.values())

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    M = 1000
    # data = aoc.get_input('input0.txt')
    # M = 10
    
    coords = parsing(data)
    # print(coords)
    N = len(coords)

    # Part I    

    heap = []

    for i, j in combinations(range(N), 2):
        junc1 = np.array(coords[i])
        junc2 = np.array(coords[j])
        d = np.sqrt(np.sum((junc1 - junc2)**2))
        heapq.heappush(heap, (d, i, j))

    dsu  = DSU(N)

    counter = 0

    while dsu.components > 1:
        counter += 1
        d, i, j = heapq.heappop(heap)

        dsu.union(i, j)
        
        if counter == M:
            comps = dsu.extract_components()
    
    len_comps = sorted([len(comp) for comp in comps])
    ans1 = len_comps[-1]*len_comps[-2]*len_comps[-3]

    print(f'Answer to part 1: {ans1}')

    # Part II

    ans2 = coords[i][0] * coords[j][0]
    
    print(f'Answer to part 2: {ans2}')
