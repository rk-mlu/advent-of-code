""" Advent of Code 2023 -- Day 15 -- """
year = 2023
day = 15     # set day!

import sys
sys.path.append('../../aux')
import aoc
from collections import defaultdict
# import numpy as np

def parsing(data):
    # parser for the input data    
    line = data.split(',')

    return line

def hash_algo(string):
    res = 0

    for s in string:
        n = ord(s)
        res += n
        res *= 17
        res = res % 256

    return res

def parse2(strings):
    operations = []
    for s in strings:
        if '-' in s:
            i = s.index('-')
        if '=' in s:
            i = s.index('=')

        lab = s[:i]
        op = s[i]

        if len(s)>i+1:
            n = int(s[i+1:])
        else :
            n = None
        operations.append((lab, op, n))

    return operations

def focusing_power(boxes):
    power = 0
    for j in range(256):
        for l, lab in enumerate(boxes[j].keys()):
            power += (j+1)*(l+1)*boxes[j][lab]
    
    return power

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    strings = parsing(data)

    # Part I    
    
    ans1 = 0

    for s in strings:
        ans1 += hash_algo(s)

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ops = parse2(strings)

    boxes = defaultdict(dict)

    for step in ops:
        num = hash_algo(step[0])
        op = step[1]
        foc = step[2]
    
        if op == '=':
            boxes[num][step[0]] = foc

        if op =='-':
            if step[0] in boxes[num].keys():
                del boxes[num][step[0]]
    
    ans2 = focusing_power(boxes)
    
    print(f'Answer to part 2: {ans2}')

