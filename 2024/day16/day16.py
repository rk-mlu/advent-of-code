""" Advent of Code 2024 -- Day 16 -- """
year = 2024
day = 16     # set day!

import sys
sys.path.append('../../aux')
import aoc
from queue import PriorityQueue
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    return lines

def find_S_E(maze):
    for m, line in enumerate(maze):
        for n, c in enumerate(line):
            if c == 'S':
                S = (m,n)
            if c == 'E':
                E = (m,n)

    return S, E

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
    # return cost

def dijkstra_set(get_nbs, start, end):
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
        # if vertex in end:
        #     break
        for nb, dist in get_nbs(vertex):
            if nb in visited:
                continue

            old_cost = cost.get(nb, float('inf'))
            new_cost = cost[vertex] + dist
            if new_cost < old_cost:
                unexplored.put((new_cost, nb))
                cost[nb] = new_cost
                parents[nb] = [vertex]
            elif new_cost == old_cost:
                parents[nb].append(vertex)

    return parents, cost


def make_path(parents, cost, goal):
    if goal not in parents:
        return None
    todo = [goal]
    path = set()
    while len(todo) > 0:   
        v = todo.pop()
        path.add(v[:2])
        if parents[v] is None:
            # start is only vertex with None parent
            continue
        for w in parents[v]:
            if w[2:] not in path:
                todo.append(w)
    return path

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    maze = parsing(data)
    
    S, E = find_S_E(maze)
    ends = []
    for j in range(4):
        ends.append((E[0], E[1], j))

    def get_nbs(pos):
        dirs = {0: (0,1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}

        nbs = []
        
        cand_forw = (pos[0] + dirs[pos[2]][0], pos[1] + dirs[pos[2]][1], pos[2])
        if maze[cand_forw[0]][cand_forw[1]] != '#':
            nbs.append((cand_forw, 1))
        
        cand_rot1 = (pos[0], pos[1], (pos[2] + 1) % 4)
        cand_rot2 = (pos[0], pos[1], (pos[2] - 1) % 4)
        nbs.append((cand_rot1, 1000))
        nbs.append((cand_rot2, 1000))
        return nbs


    # Part I    

    parents, cost = dijkstra(get_nbs, (S[0], S[1], 0), ends)
    
    for E in ends:
        res = cost.get(E, -1)
        if res != -1:
            ans1 = res

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0

    parents, cost = dijkstra_set(get_nbs, (S[0], S[1], 0), ends)
    
    for E in ends:
        res = cost.get(E, -1)
        if res != -1:
            path = make_path(parents, cost, E)
            ans2 = len(path)
            
    print(f'Answer to part 2: {ans2}')
