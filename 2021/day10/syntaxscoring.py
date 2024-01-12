""" Advent of Code 2021 -- Day 10 -- """
year = 2021
day = 10     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np
from collections import deque

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    return lines

def corrupted(line):

    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    pairs = {')':  '(', ']': '[', '}': '{', '>': '<'}
    
    queue = deque()

    pts = 0
    for c in line:
        if c in ['(', '[', '{', '<']:
            queue.append(c)
        else :
            last_c = queue.pop()

            if pairs[c] != last_c:
                pts = points[c]
    
    return pts

def autocomplete(line):

    pairs = {'(': ')', '[':']', '{': '}', '<': '>'}
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    
    queue = deque()

    for c in line:
        if c in ['(', '[', '{', '<']:
            queue.append(c)
        else :
            last_c = queue.pop()

            if pairs[last_c] == c:
                continue
    
    pts = 0
    while queue:
        c = queue.pop()
        pts = 5*pts + points[pairs[c]]
    
    return pts


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    lines = parsing(data)

    # Part I    

    ans1 = 0
    for line in lines:
        ans1 += corrupted(line)

    print(f'Answer to part 1: {ans1}')

    # Part II
   
    pts = [autocomplete(line) for line in lines if not corrupted(line)]
    
    pts.sort()
    ans2 = pts[(len(pts) - 1)//2]

    print(f'Answer to part 2: {ans2}')
