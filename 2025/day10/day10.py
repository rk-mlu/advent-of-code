""" Advent of Code 2025 -- Day 10 -- """
year = 2025
day = 10         # set day!

import sys
sys.path.append('../../aux')
import aoc
from ast import literal_eval
import numpy as np
from scipy.optimize import milp
from scipy.optimize import LinearConstraint

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    lights = []
    list_buttons = []
    jolts = []

    for line in lines:
        words = line.split()
        
        num_lights = len(words[0]) - 2
        light = [0]*num_lights
        
        for j, c in enumerate(words[0][1:-1]):
            if c == '#':
                light[j] = 1
        
        lights.append(tuple(light))

        buttons = []
        for w in words[1:-1]:
            s = literal_eval(w)
            if type(s) is int:
                buttons.append((s,))
            else :
                buttons.append(s)

        list_buttons.append(buttons)
        jolt = [int(c) for c in words[-1][1:-1].split(',')]
        jolts.append(jolt)


    return lights, list_buttons, jolts


"""
Implementierung des Dijkstra Algorithmus
Kürzester Weg in einem gewichteten Graphen mit pos. Gewichten
"""

from queue import PriorityQueue

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
        if vertex == end:
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

def make_path(parents, goal):
    if goal not in parents:
        return None
    v = goal
    path = []
    while v is not None:    # start is only vertex with None parent
        path.append(v)
        v = parents[v]
    path.reverse()
    return path


def get_neighbors(node, buttons):
    neighbs = []

    for button in buttons:
        nb = list(node)
        for b in button:
            nb[b] = 1 - nb[b]
        neighbs.append((tuple(nb), 1))

    return neighbs


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input0.txt')
    
    lights, list_buttons, jolts = parsing(data)

    # Part I    
    ans1 = 0

    for light, buttons in zip(lights, list_buttons):
        start = tuple([0]*len(light))
        get_nbs = lambda x: get_neighbors(x, buttons)
        par, cost = dijkstra(get_nbs, start, light)
        ans1 += cost[light]

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    

    for buttons, jolt in zip(list_buttons, jolts):
        N = len(jolt)
        M = len(buttons)

        c = np.ones(M, dtype=int)
        A = np.zeros((N,M), dtype=int)

        # print(light)

        for j, button in enumerate(buttons):
            # print(button)
            for b in button:
                A[b, j] = 1

        print(A)
        b_u = np.array(jolt, dtype=int)
        b_l = b_u.copy()
        integrality = np.ones_like(c)
        
        constraints = LinearConstraint(A, b_l, b_u)
        res = milp(c=c, constraints=constraints, integrality=integrality)
    
        print(res.x)
        ans2 += int(np.sum(res.x))

    
    print(f'Answer to part 2: {ans2}')
