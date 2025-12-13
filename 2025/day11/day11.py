""" Advent of Code 2025 -- Day 11 -- """
year = 2025
day = 11         # set day!

import sys
sys.path.append('../../aux')
import aoc
# from functools import cache
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    outs = dict()

    for line in lines:
        out_node, in_nodes = line.split(': ')
        in_nodes = in_nodes.split()
        outs.setdefault(out_node, [])
        for in_node in in_nodes:
            outs[out_node].append(in_node)

    return outs

cache = dict()

def num_path(node, goal, p, outs):
    if node == goal:
        cache.setdefault((node,goal,p), 1)
        return 1
    elif (node,goal,p) in cache.keys():
        return cache[(node,goal,p)]
    else: 
        res = 0
        for nb in outs.get(node, []):
            x = cache.setdefault((nb,goal,p), num_path(nb, goal, p, outs))
            res += x
        cache[(node,goal,p)] = res
        return res


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input0.txt')
    
    outs = parsing(data)
    
    # Part I    

    ans1 = num_path('you', 'out', 1, outs)
    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 1

    ans2 *= num_path('svr', 'fft', 2, outs)
    print(ans2)
    ans2 *= num_path('fft', 'dac', 2, outs)
    print(ans2)
    ans2 *= num_path('dac', 'out', 2, outs)
    print(ans2)
    
    print(f'Answer to part 2: {ans2}')
