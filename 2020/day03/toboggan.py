""" Advent of Code 2020 -- Day 03 -- """
year = 2020
day = 3     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    return lines

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    lines = parsing(data)
    
    forest = []
    num_rows = 0
    for line in lines:
        trees = [0 if x == '.' else 1 for x in line]
        forest.append(trees)
        num_rows += 1

    # Part I    
    
    steps_right = 3
    m = len(forest[0])
    ans1 = 0

    for j in range(num_rows):
        pos_r = steps_right*j % m
        ans1 += forest[j][pos_r]

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    steps = [ (1,1), (3,1), (5,1), (7,1), (1,2)]

    num_trees = []

    ans2 = 1
    for r, d in steps:
        ans = 0
        for j in range(num_rows//d):
            pos_r = r*j % m
            ans += forest[d*j][pos_r]
        ans2 *= ans

    print(f'Answer to part 2: {ans2}')
