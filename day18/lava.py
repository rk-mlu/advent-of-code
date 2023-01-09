""" Advent of Code 2022 -- Day 18 -- """

import aoc
import ast
from itertools import combinations
from copy import deepcopy
# import numpy as np

def parsing(data):
    lines = data.splitlines()
    
    pixels = set()
    for line in lines:
        pixels.add(ast.literal_eval(line))
    
    # print(pixels)
    return pixels

def get_neighbors(p):
    deltas = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

    neighbors = set()

    for d in deltas:
        nb = (p[0] + d[0], p[1] + d[1], p[2] + d[2])
        neighbors.add(nb)

    return neighbors

def check_neighbors(p, pixels):
    neighbors = get_neighbors(p)
    num_nbs = len(pixels.intersection(neighbors))

    return num_nbs

def get_boundary(pixels):
    boundary = set()

    for p in pixels:
        neighbors = get_neighbors(p)
        boundary.update(neighbors.difference(pixels))
   
    return boundary


def partition_boundary(pixels, boundary):
    part_boundary = []
    
    boundary2 = boundary.copy()
    for b in boundary:
        if b not in boundary2:
            continue
        part_b = set()
        part_b.add(b)
        boundary2.remove(b)
        
        neighbors_b = set()

        neighbors_b1 = get_neighbors(b)
        neighbors_b1.difference_update(pixels)
        neighbors_b = neighbors_b.union(neighbors_b1)
        for nb in neighbors_b1:
            neighbors_b2 = get_neighbors(nb)
            neighbors_b2.difference_update(pixels)
            neighbors_b = neighbors_b.union(neighbors_b2)
            for nb2 in neighbors_b2:
                neighbors_b3 = get_neighbors(nb2)
                neighbors_b3.difference_update(pixels)
                neighbors_b = neighbors_b.union(neighbors_b3)


        part_b = part_b.union(neighbors_b)
        boundary2.difference_update(neighbors_b)
        part_boundary.append(part_b)

    merged = merge(part_boundary)

    return merged
 
def merge(part_boundary):
    part_boundary2 = deepcopy(part_boundary)
    merged = []
    for B1, B2 in combinations(part_boundary, 2):
        if B1 in part_boundary2 and B2 in part_boundary2 and len(B1.intersection(B2)) > 0:
            merged.append(B1.union(B2))
            part_boundary2.remove(B1)
            part_boundary2.remove(B2)

    for B in part_boundary2:
        merged.append(B)

    if len(part_boundary) > len(merged):
        merged = merge(merged)

    return merged

    
    

if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    # Part I    
    pixels = parsing(data)

    surface = 0

    for p in pixels:
        num_nbs = check_neighbors(p, pixels)
        surface += 6 - num_nbs

    print(f'Part I: The total surface area is {surface}')
    
    # Part II
    boundary = get_boundary(pixels)

    # partition boundary in connected parts
    part_bdd = partition_boundary(pixels, boundary)
    
    # determine outside boundary (should be set with most elements)
    max_ind = 0
    max_val = len(part_bdd[max_ind])
    for j, pd in enumerate(part_bdd):
        if max_val < len(part_bdd):
            max_ind = j

    interior = set()
    
    for b in boundary:
        if b not in part_bdd[max_ind]:
            interior.add(b)
            continue

    surface2 = 0
    pixels2 = pixels.union(interior)

    for p in pixels:
        num_nbs = check_neighbors(p, pixels2)
        surface2 += 6 - num_nbs

    print(f'Part II: The exterior surface area is {surface2}')

