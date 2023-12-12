""" Advent of Code 2023 -- Day 12 -- """
year = 2023
day = 12     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    springs = []
    groups = []

    for line in lines:
        s, g = line.split()
        springs.append(s)
        gr = [int(n) for n in g.split(',')]
        groups.append(gr)

    return springs, groups

def trim_springs(s):
    ts = s

    if ts[0] == '.':
        ts = trim_springs(ts[1:])

    if ts[-1] == '.':
        ts = trim_springs(ts[:-1])
    
    if '..' in ts:
        i = ts.index('..')
        ts = trim_springs(ts[:i] + ts[i+1:])

    return ts

def fix_springs(s, gr):
    fs = s
    n = len(fs) -1
    if fs[0] == '#':
        for j in range(1,gr[0]):
            c = fs[j]
            if c == '?':
                fs = fs[:j] + '#' + fs[j+1:]
        fs = fs[:gr[0]] + '.' + trim_springs(fs[gr[0]+1:])
    if fs[-1] == '#':
        for j in range(1,gr[-1]):
            c = fs[n - j]
            if c == '.':
                print("error")
            if c == '?':
                fs = fs[:n-j] + '#' + fs[n-j+1:]
        fs = trim_springs(fs[:n-gr[-1]]) + '.' + fs[n-gr[-1]+1:]
    return  fs


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    springs, groups = parsing(data)
    

    # Part I    

    ans1 = 0
    
    for s, g in zip(springs, groups):
        ts = trim_springs(s)
        fs = fix_springs(ts, g) 
        print(s, fs, g)

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    
    print(f'Answer to part 2: {ans2}')
