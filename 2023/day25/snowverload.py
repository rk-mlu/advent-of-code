""" Advent of Code 2023 -- Day 25 -- """
year = 2023
day = 25     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
from collections import defaultdict
from itertools import combinations, pairwise
import heapq
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    wiring = defaultdict(set)
    for line in lines:
        comp, others = line.split(': ')
        others = others.split()
        for comp2 in others:
            wiring[comp].add(comp2)
            wiring[comp2].add(comp)

    return wiring

def enumerate_nodes(wiring):

    nodes = dict()

    for j, node in enumerate(wiring.keys()):
        nodes[node] = j

    return nodes

def part1(wiring):
    N = len(wiring)
    nodes = enumerate_nodes(wiring)

    graph = np.zeros( (N,N), dtype = int)

    for node1 in wiring.keys():
        for node2 in wiring[node1]:
            graph[nodes[node1], nodes[node2]] = 1
   

    for i in range(3):
        print(f'Searching for wire {i+1}... (takes a few minutes)')
        dist, prev = dijkstra_allpairs(graph)
        traffic = get_traffic(graph, prev)
        # print(traffic)

        k, l = np.unravel_index(np.argmax(traffic), traffic.shape)
        # print(f'{i+1}: ({k}, {l})')
        
        graph[k,l] = 0
        graph[l,k] = 0
    
    graph = csr_matrix(graph)

    n_components, labels = connected_components(graph, directed=False,
            return_labels=True)
    
    return np.sum(labels)*(len(labels) - np.sum(labels))

def dijkstra_allpairs(graph):

    N, _ = graph.shape
    
    dist = np.zeros((N,N), dtype=int)
    prev = np.zeros((N,N), dtype=int)

    for source in range(N):

        Q = []
        visited = set()
        
        dist[source, source] = 0
        prev[source, source] = -9999
        heapq.heappush(Q, (dist[source,source], source))
        
        for v in range(N):
            if v != source:
                dist[source, v] = 2*N
                prev[source, v] = -2*N
                heapq.heappush(Q, (dist[source,v], v))

        while len(Q) > 0:
            p, u = heapq.heappop(Q)
            if u in visited:
                continue
            else :
                visited.add(u)
            
            nbs = np.argwhere(graph[u,:])

            for k in range(len(nbs)):
                nb = nbs[k]
                alt = dist[source, u] + 1
                if alt < dist[source, nb]:
                    dist[source, nb] = alt
                    prev[source, nb] = u
                    heapq.heappush(Q, (dist[source,nb], nb[0]))
    
    return dist, prev    

def get_traffic(graph, prev):
    N,_ = graph.shape

    traffic = np.zeros((N,N), dtype=int)
    
    for source, goal in combinations(range(N),2):
        path = [goal]
        current = goal
        while current != source:
            current = prev[source, current]
            path.append(current)

        for n1, n2 in pairwise(path):
            traffic[n1, n2] += 1
            traffic[n2, n1] += 1

    return traffic

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    wiring = parsing(data)
    # print(len(wiring))

    # Part I    
    num_connection = 0
    for comp in wiring.keys():
        num_connection += len(wiring[comp])
    
    # print(num_connection)

    ans1 = part1(wiring)
    print(f'Answer to part 1: {ans1}')

    # Part II
    
    # ans2 = 0
    # print(f'Answer to part 2: {ans2}')
