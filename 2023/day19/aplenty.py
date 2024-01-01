""" Advent of Code 2023 -- Day 19 -- """
year = 2023
day = 19     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
# from itertools import product

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

def part2(lim, wf):

    state = 'in'
    interval = np.array([1, lim, 1, lim, 1, lim, 1, lim], dtype=int)
   
    Q = [(state, interval)]
    accepted = []
    rejected = []
    
    while len(Q) > 0:
        st, ival = Q.pop(0)
        
        res = apply_rules(st, ival, wf)

        for s, new_ival in res:
            if s == 'A':
                accepted.append(new_ival)
            elif s == 'R':
                rejected.append(new_ival)
            else :
                Q.append((s, new_ival))

    print(accepted)

    ans2 = 0
    for ival in accepted:
        p = 1
        for j in range(4):
            p *= (ival[2*j+1] - ival[2*j] + 1)
            if p <= 0:
                print(p)
        ans2 += p
    ans2b = 0
    for ival in rejected:
        p = 1
        for j in range(4):
            p *= (ival[2*j+1] - ival[2*j] + 1)
        ans2b += p
    print(4000**4-ans2-ans2b)
    return ans2
    

def apply_rules(state, ival, wf):

    done = []

    # if state == 'A':
    #     done.append(('A', ival))
    # elif state == 'R':
    #     done.append(('R', ival))
    # else :
    ind = dict()
    ind['x'] = 0
    ind['m'] = 1
    ind['a'] = 2
    ind['s'] = 3

    for rule in wf[state]:
        if ':' in rule:
            cond, new_state = rule.split(':')
            i = ind[cond[0]]
            bound = int(cond[2:])
            ival1 = ival.copy()
            
            if cond[1] == '>':
                ival1[2*i] = max(ival1[2*i], bound + 1)
                
                if ival1[2*i] <= ival1[2*i+1]:
                    done.append((new_state, ival1))
                    ival[2*i+1] = bound

            if cond[1] == '<':
                ival1[2*i+1] = min(ival1[2*i+1], bound - 1)
                
                if ival1[2*i] <= ival1[2*i+1]:
                    done.append((new_state, ival1))
                    ival[2*i] = bound

        else :
            done.append((rule, ival))
            
    return done


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    wf, parts = parsing(data)
    
    # Part I    

    ans1 = 0

    for p in parts:
        if process_part(p, 'in', wf):
            ans1 += p['x'] + p['m'] + p['a'] + p['s']

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    lim = 4000

    ans2 = part2(lim, wf)
        
    print(f'Answer to part 2: {ans2}')
