""" Advent of Code 2023 -- Day 19 -- """
year = 2023
day = 19     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np
from itertools import product

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    workflows = dict()
    ratings = []

    blank_line = False
    
    for line in lines:
        if len(line) == 0:
            blank_line = True
            continue

        if not blank_line:
            i = line.index('{')
            key = line[:i]
            rules = line[i+1:-1].split(',')
            workflows[key] = rules
        else :
            rt = line[1:-1].split(',')
                
            part = dict()


            for r in rt:
                part[r[0]] = int(r[2:])

            ratings.append(part)

    return workflows, ratings

def process_part(part, state, workflows):
    
    if state == 'R':
        return False
    if state == 'A':
        return True
    
    for rule in workflows[state]:
        if ':' not in rule:
            return process_part(part, rule, workflows)
        else :
            cond, new_state = rule.split(':')
            
            if cond[1] == '<':
                if part[cond[0]] < int(cond[2:]):
                    return process_part(part, new_state, workflows)
            elif cond[1] == '>':
                if part[cond[0]] > int(cond[2:]):
                    return process_part(part, new_state, workflows)
            else :
                print(cond[1])


if __name__ == '__main__':
    # data = aoc.dl_data(day, year, 'input1.txt')                                  
    data = aoc.get_input('input2.txt')
    
    wf, parts = parsing(data)

    # Part I    

    ans1 = 0

    for p in parts:
        if process_part(p, 'in', wf):
            ans1 += p['x'] + p['m'] + p['a'] + p['s']

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    x = 1
    p=dict()
    # for (x,m,a,s) in product(range(1,4001), repeat=4):
    for (m,a,s) in product(range(1,4001), repeat=3):
        p['x'] = x
        p['m'] = m
        p['a'] = a
        p['s'] = s
        # print(p)
        if process_part(p, 'in', wf):
            ans2 += p['x'] + p['m'] + p['a'] + p['s']

    print(f'Answer to part 2: {ans2}')
