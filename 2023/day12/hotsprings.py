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

def count_arrangement(s, gr, hashtab):
    grt = tuple(gr)
    if (s,grt) in hashtab.keys():
        return hashtab[(s,grt)]

    if len(gr) == 0:
        if '#' in s:
            hashtab[(s,grt)] = 0
            return 0
        else :
            hashtab[(s,grt)] = 1
            return 1

    num_springs = sum(gr)
    if (s.count('#') + s.count('?')) < num_springs:
        hashtab[(s,grt)] = 0
        return 0

    if len(s) < num_springs + len(gr) - 1:
        hashtab[(s,grt)] = 0
        return 0

    if s[0] == '.':
        n = count_arrangement(s[1:], gr, hashtab)
        hashtab[(s,grt)] = n
        return n

    if s[0] == '?':
        b = count_arrangement('#'+s[1:], gr, hashtab)
        a = count_arrangement(s[1:], gr, hashtab)

        hashtab[(s,grt)] = a + b
        return a + b
    
    if s[0] == '#':
        if '.' in s[:gr[0]]:
            hashtab[(s,grt)] = 0
            return 0
        if len(s) == gr[0]:
            if len(gr) == 1:
                hashtab[(s,grt)] = 1
                return 1
            else :
                hashtab[(s,grt)] = 0
                return 0
        
        if s[gr[0]] == '#':
            hashtab[(s,grt)] = 0
            return 0
        else :
            n = count_arrangement(s[gr[0]+1:], gr[1:],hashtab)
            hashtab[(s,grt)] = n
            return n

    return 0

def unfold(s, g):
    new_g = 5*g
    new_s = 4*(s+'?') + s

    return new_s, new_g


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    springs, groups = parsing(data)

    # Part I    

    ans1 = 0
    
    hashtab = dict()
    for s, g in zip(springs, groups):
        n = count_arrangement(s, g, hashtab)
        ans1 += n

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    for s, g in zip(springs, groups):
        s2, g2 = unfold(s,g)
        n = count_arrangement(s2, g2, hashtab)
        ans2 += n

    print(f'Answer to part 2: {ans2}')
