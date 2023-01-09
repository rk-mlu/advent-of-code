""" Advent of Code 2022 -- Day 18 -- """

import aoc
import ast
# import numpy as np

def parsing(data):
    lines = data.splitlines()
    
    pixels = set()
    for line in lines:
        pixels.add(ast.literal_eval(line))
    
    # print(pixels)
    return pixels

def check_neighbors(p, pixels):
    deltas = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

    num_nbs = 0
    for d in deltas:
        nb = (p[0] + d[0], p[1] + d[1], p[2] + d[2])
        if nb in pixels:
            num_nbs += 1

    return num_nbs


if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    # Part I    
    pixels = parsing(data)

    surface = 0

    for p in pixels:
        num_nbs = check_neighbors(p, pixels)
        surface += 6 - num_nbs

    print(f'Part I: The surface area is {surface}')
    
    # Part II
