""" Advent of Code 2024 -- Day 18 -- """
year = 2024
day = 18     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
from queue import PriorityQueue

def parsing(data, M, N, lim):
    # parser for the input data    
    lines = data.splitlines()
    len
    
    maze = np.zeros((M+2,N+2), dtype = int)
    maze[0,  :] = 1
    maze[-1, :] = 1
    maze[:,  0] = 1
    maze[:, -1] = 1

    for k, line in enumerate(lines):
        if k == lim:
            break
        m, n = line.split(',')
        m = int(m) + 1
        n = int(n) + 1

        maze[m, n] = 1

    return maze.T, lines

def dijkstra(get_nbs, start, end):
    """ Dijkstra algorithm 
    Quelle: https://gist.github.com/qpwo/cda55deee291de31b50d408c1a7c8515
    """
    visited = set()
    cost = {start: 0}
    parents = {start: None}
    unexplored = PriorityQueue()

    unexplored.put((0, start))

    while unexplored:
        while not unexplored.empty():
            # get vertex with lowest cost
            _, vertex = unexplored.get()
            if vertex not in visited:
                break
        else :
            break
        if vertex in end:
            break
        for nb, dist in get_nbs(vertex):
            if nb in visited:
                continue

            old_cost = cost.get(nb, float('inf'))
            new_cost = cost[vertex] + dist
            if new_cost < old_cost:
                unexplored.put((new_cost, nb))
                cost[nb] = new_cost
                parents[nb] = vertex
    return parents, cost

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
   
    M, N, lim = 71, 71, 1024
    # M, N, lim = 7, 7, 12
    maze, lines = parsing(data, M, N, lim)
    start = (1,1)
    end = (M, N)

    # Part I    

    ans1 = 0
    
    def get_nbs(pos):
        dirs = {0: (0,1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}
        
        nbs = []

        for d in range(4):
            cand = (pos[0]+dirs[d][0], pos[1] + dirs[d][1])
            if maze[cand[0], cand[1]] != 1:
                nbs.append((cand, 1))
        return nbs

    parents, cost = dijkstra(get_nbs, start, end)
    
    ans1 = cost.get(end, -1)

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    min_bytes = 1024
    max_bytes = 3450
    
    res = {1024: 354, 3450: -1}

    cur = (max_bytes + min_bytes)//2
    searching = True

    while searching:
        maze, lines = parsing(data, M, N, cur)
        
        def get_nbs(pos):
            dirs = {0: (0,1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}
        
            nbs = []

            for d in range(4):
                cand = (pos[0]+dirs[d][0], pos[1] + dirs[d][1])
                if maze[cand[0], cand[1]] != 1:
                    nbs.append((cand, 1))
            return nbs

        parents, cost = dijkstra(get_nbs, start, end)
        
        steps = cost.get(end, -1)

        res[cur] = steps

        if steps == -1:
            max_bytes = cur
            cur = (max_bytes + min_bytes)//2
        else :
            min_bytes = cur
            cur = (max_bytes + min_bytes)//2
            
        if max_bytes == min_bytes + 1:
            break
        
    print(res)
    ans2 = lines[max_bytes-1]
    
    print(f'Answer to part 2: {ans2}')
