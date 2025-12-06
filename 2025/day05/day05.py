""" Advent of Code 2025 -- Day 5 -- """
year = 2025
day = 5         # set day!

import sys
sys.path.append('../../aux')
import aoc
import bisect
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    ranges = []
    IDs = []
    for line in lines:
        if '-' in line:
            s, e = line.split('-')
            ranges.append((int(s), int(e)))
        elif len(line) > 0:
            IDs.append(int(line))

    return ranges, IDs

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input0.txt')
    
    ranges, IDs = parsing(data)

    # Part I    

    ans1 = 0

    for i in IDs:
        for s,e in ranges:
            if i >= s and i <= e:
                ans1 += 1
                break

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    bounds = []

    for s,e in ranges:
        # print(s,e)
        if e < s:
            continue
        e += 1 # make intervals half open
        if len(bounds) == 0:
            bounds.append(s)
            bounds.append(e)
        else :
            pos_s = bisect.bisect_left(bounds, s)
            pos_e = bisect.bisect_left(bounds, e)

            if pos_s % 2 == 1:
                s = bounds[pos_s-1]
                start = pos_s - 1
            else :
                start = pos_s
            
            if pos_e % 2 == 1 and pos_e < len(bounds):
                e = bounds[pos_e]
                stop = pos_e + 1
            else :
                stop = pos_e

            bounds[start:stop] = [s, e]

        # print(bounds)

    for j in range(len(bounds)//2):
        ans2 += bounds[2*j+1] - bounds[2*j]
    
    print(f'Answer to part 2: {ans2}')
