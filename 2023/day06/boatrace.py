""" Advent of Code 2023 -- Day 06 -- """

import sys
sys.path.append('../../aux')
import aoc
from math import sqrt, ceil, floor
# import numpy as np

def parse(lines):
    times  = [int(t) for t in lines[0].split()[1:]]
    dists  = [int(d) for d in lines[1].split()[1:]]

    return times, dists

def parse2(lines):
    times  = [t for t in lines[0].split()[1:]]
    dists  = [d for d in lines[1].split()[1:]]
    
    time = ''
    for t in times:
        time += t
    time = int(time)

    record = ''
    for r in dists:
        record += r
    record = int(record)

    return time, record

def num_records(time, record):
    num = 0
    for t in range(time):
        dist = t*(time-t)
        if dist > record:
            num += 1
    return num

if __name__ == '__main__':
    data = aoc.get_input('input1.txt')                                  
    lines = data.splitlines()

    # Part I 
    times, records = parse(lines)
    ans1 = 1
    for (t,r) in zip(times, records):
        ans1 *= num_records(t, r)

    print(f'Answer to part 1: {ans1}')

    # Part II
    # data = aoc.get_input('input2.txt')
    time, record = parse2(lines)

    bdd_t = (ceil(time/2 - sqrt(time**2/4 - record)),
             floor(time/2 + sqrt(time**2/4 - record)))
    print(bdd_t)
    
    ans2 = bdd_t[1] - bdd_t[0] + 1 
    
    print(f'Answer to part 2: {ans2}')
