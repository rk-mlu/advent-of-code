""" Advent of Code 2023 -- Day 23 -- """
year = 2023
day = 23     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    graph = dict()
    for p, c in enumerate(lines[0]):
        if c == '.':
            spos = (0,p)
            graph[spos] = [(1,p)]
            break
    
    for p, c in enumerate(lines[-1]):
        if c == '.':
            goal = (len(lines)-1,p)
            graph[goal] = [(goal[0]-1, p)]
            break
    
    nodes = {spos, goal}

    for i, line in enumerate(lines[1:-1], start=1):
        for j, c in enumerate(line[1:-1], start=1):
            if c == '.':
                graph[(i,j)] = []
                counter = 0
                for d in [(1,0, '^'), (-1,0,'v'), (0,1,'<'), (0,-1,'>')]:
                    cand = (i+d[0], j+d[1])
                    if lines[i+d[0]][j+d[1]] == '.':
                        counter += 1
                    if lines[i+d[0]][j+d[1]] not in ['#',d[2]]:
                        graph[(i,j)].append(cand)
                if counter == 0:
                    nodes.add((i,j))
            if c == '<':
                graph[(i,j)] = [(i,j-1)]
                if lines[i][j-1] == '#':
                    print('error')
            if c == '>':
                graph[(i,j)] = [(i,j+1)]
                if lines[i][j+1] == '#':
                    print('error')
            if c == 'v':
                graph[(i,j)] = [(i+1,j)]
                if lines[i+1][j] == '#':
                    print('error')
            if c == '^':
                graph[(i,j)] = [(i-1,j)]
                if lines[i-1][j] == '#':
                    print('error')

    return spos, goal, graph, nodes

def get_nb(node, nodes, graph):
    
    list_nb = []
    nbs = graph[node]

    for nb in nbs:
        old = node
        current = nb
        weight = 1
        while current not in nodes:
            if len(graph[current]) == 1 and graph[current][0] == old:
                return []
            for cand in graph[current]:
                if cand != old:
                    old = current
                    current = cand
                    weight += 1
                    break
        list_nb.append((current,weight)) 
    
    return list_nb

def decompose(nodes, graph):
    
    edges = []
    
    for n in nodes:
        nbs = get_nb(n, nodes, graph)
        
        for nb,w in nbs:
            edges.append((n, nb, w))

    return edges

def bellmanford(vertices, graph, source, goal):

    edges = decompose(vertices, graph)

    V = len(vertices)
    
    dist = dict()
    pred = dict()

    for v in vertices:
        dist[v] = np.inf
        pred[v] = None
    
    dist[source] = 0

    for n in range(V-1):
        for u,v,w in edges:
            if dist[u] < (dist[v] + w):
                dist[v] = dist[u] - w
                pred[v] = u

    for (u,v,w) in edges:
        if dist[u] < (dist[v] + w):
            pred[v] = u
            visited = dict()
            visited[v] = True
            while u not in visited.keys():
                visited[u] = True
                u = pred[u]
            ncycle = [u]
            v = pred[u]
            while v != u:
                ncycle.append(v)
                v = pred[v]
            print('Error: Graph contains a negative-weight cycle')
            print(ncycle)

    return -dist[goal]

def parsing2(data):
    # parser for the input data    
    lines = data.splitlines()

    graph = dict()
    for p, c in enumerate(lines[0]):
        if c == '.':
            spos = (0,p)
            graph[spos] = [(1,p)]
            break
    
    for p, c in enumerate(lines[-1]):
        if c == '.':
            goal = (len(lines)-1,p)
            graph[goal] = [(goal[0]-1, p)]
            break
    
    nodes = {spos, goal}

    for i, line in enumerate(lines[1:-1], start=1):
        for j, c in enumerate(line[1:-1], start=1):
            if c != '#':
                graph[(i,j)] = []
                counter = 0
                for d in [(1,0, '^'), (-1,0,'v'), (0,1,'<'), (0,-1,'>')]:
                    cand = (i+d[0], j+d[1])
                    if lines[i+d[0]][j+d[1]] == '.':
                        counter += 1
                    if lines[i+d[0]][j+d[1]] not in ['#']:
                        graph[(i,j)].append(cand)
                if counter == 0:
                    nodes.add((i,j))

    return spos, goal, graph, nodes


def get_nb2(node, nodes, graph):
    
    list_nb = []
    nbs = graph[node]

    for nb in nbs:
        old = node
        current = nb
        weight = 1
        while current not in nodes:
            for cand in graph[current]:
                if cand != old:
                    old = current
                    current = cand
                    weight += 1
                    break
        list_nb.append((current,weight)) 
    
    return list_nb

def decompose2(nodes, graph, source, goal):
    
    edges = dict()
    get_nbs = dict()

    get_nbs[goal] = set()

    second_last_node, w_last = get_nb2(goal, nodes, graph)[0]
    edges[(second_last_node, goal)] = w_last
    get_nbs[second_last_node] = {goal}

    for n in nodes:
        if n == goal or n == second_last_node:
            continue
        nbs = get_nb2(n, nodes, graph)
        get_nbs[n] = set()
        
        for nb,w in nbs:
            if nb != source:
                get_nbs[n].add(nb)
                edges[(n,nb)] = w
    
    return edges, get_nbs

def find_long_path(source, goal, nodes, edges, get_nbs):
    
    
    def gen_paths(path, visited):
        current = path[-1][0]
        l = path[-1][1]
        new_path = []
        if current != goal:
            nbs = get_nbs[current]
            for nb in nbs:
                if nb not in visited:
                    new_visited = visited.copy()
                    new_visited.add(nb)
                    new_path2 = path.copy()
                    new_path2.append((nb, path[-1][1] + edges[(current,nb)]))
                    new_l, new_path2 = gen_paths(new_path2, new_visited)
                    if new_l > l:
                        # print(new_l)
                        l = new_l
                        new_path = new_path2
        return l, new_path

    visited = {source}
    path = [(source,0)]

    l, path = gen_paths(path, visited)
    
    
    return l



if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    spos, goal, graph, nodes = parsing(data)

    # Part I    
    
    ans1 = bellmanford(nodes, graph, spos, goal)
    print(f'Answer to part 1: {ans1}')

    # Part II
    spos, goal, graph, nodes = parsing2(data)
    
    edges, get_nbs = decompose2(nodes, graph, spos, goal)
    
    ans2 = find_long_path(spos, goal, nodes, edges, get_nbs)
    
    print(f'Answer to part 2: {ans2}')
