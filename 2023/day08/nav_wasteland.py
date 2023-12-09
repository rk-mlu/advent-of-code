""" Advent of Code 2023 -- Day 08 -- """

import sys
sys.path.append('../../aux')
import aoc
from math import lcm
# import numpy as np

def parse(lines):
    instr = lines[0]
    
    network = dict()

    for line in lines[2:]:
        node = line[:3]
        network[node] = (line[7:10], line[12:15])

    return instr, network

def steps2Z(pos, instr, network):
    n = len(instr)
    steps = 0
    while pos[-1] != 'Z':

        if instr[steps % n] == 'L':
            i = 0
        elif instr[steps % n] == 'R':
            i = 1
        else :
            print("error")

        pos = network[pos][i]
        steps += 1

    return steps

if __name__ == '__main__':
    data = aoc.get_input('input1.txt')                                  
    lines = data.splitlines()
    
    # Part I    
    instr, network = parse(lines)
    
    n = len(instr)
    steps = 0
    pos = 'AAA'
    while pos != 'ZZZ':

        if instr[steps % n] == 'L':
            i = 0
        elif instr[steps % n] == 'R':
            i = 1
        else :
            print("error")

        pos = network[pos][i]
        steps += 1

    ans1 = steps

    print(f'Answer to part 1: {ans1}')

    # Part II
    data = aoc.get_input('input1.txt')
    # data = aoc.get_input('input2.txt')
    lines = data.splitlines()
    instr, network = parse(lines)

    pos_list = []
    for k in network.keys():
        if k[-1] == 'A':
            pos_list.append(k)
    
    step_list = []
    for p in pos_list:
        steps = steps2Z(p, instr, network)
        step_list.append(steps)

    # turns out, that number of steps to first Z is also the period for each
    # position. So the total number of steps is the least common multiple of
    # each step number.
    ans2 = lcm(*step_list)

    print(f'Answer to part 2: {ans2}')
