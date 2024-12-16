""" Advent of Code 2024 -- Day 15 -- """
year = 2024
day = 15     # set day!

import sys
sys.path.append('../../aux')
import aoc
from copy import deepcopy
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    warehouse = []
    instr = ""

    for m, line in enumerate(lines):
        n = line.find('@')
        if n != -1:
            start = (m,n)
        if line.startswith('#'):
            wh = [c for c in line]
            warehouse.append(wh)
        elif len(line) > 0:
            instr += line
            

    return start, warehouse, instr


def sum_gps(wh):
    M = len(wh)
    N = len(wh[0])
    
    res = 0

    for m in range(M):
        for n in range(N):
            if wh[m][n] == 'O':
                res += 100*m + n
    
    return res

def move(d, p, wh):
    moves = {'v': (1,0), '^': (-1,0), '<': (0,-1), '>': (0,1)}
    cand = (p[0]+moves[d][0], p[1]+moves[d][1])

    if wh[cand[0]][cand[1]] == 'O':
        move(d, cand, wh)

    if wh[cand[0]][cand[1]] == '.':
        wh[cand[0]][cand[1]] = wh[p[0]][p[1]]
        wh[p[0]][p[1]] = '.'
        return cand
    
    return p

def parsing2(data):
    # parser for the input data    
    lines = data.splitlines()
    
    warehouse = []
    instr = ""
    
    expend = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}


    for m, line in enumerate(lines):
        n = line.find('@')
        if n != -1:
            start = (m,2*n)
        if line.startswith('#'):
            wh = []
            for c in line:
                s = expend[c]
                for t in s:
                    wh.append(t)
            warehouse.append(wh)
        elif len(line) > 0:
            instr += line
            
    return start, warehouse, instr

def sum_gps2(wh):
    M = len(wh)
    N = len(wh[0])
    
    res = 0

    for m in range(M):
        for n in range(N):
            if wh[m][n] == '[':
                res += 100*m + n  
    return res


def move2(d, p, wh):
    moves = {'v': (1,0), '^': (-1,0), '<': (0,-1), '>': (0,1)}
    cand = (p[0]+moves[d][0], p[1]+moves[d][1])
    wh_cp = deepcopy(wh)

    if d in {'<', '>'} or wh[p[0]][p[1]] == '@':
        if wh[cand[0]][cand[1]] in {'[', ']'}:
            # print(d, cand)
            _, wh_cp = move2(d, cand, wh_cp)

        if wh_cp[cand[0]][cand[1]] == '.':
            wh_cp[cand[0]][cand[1]] = wh[p[0]][p[1]]
            wh_cp[p[0]][p[1]] = '.'
            return cand, wh_cp
        return p, wh
    else :
        # vertical movement
        if wh[p[0]][p[1]] == '[':
            offset = 1
        elif wh[p[0]][p[1]] == ']':
            offset = -1
        else :
            offset = 0
        
        p_nb = (p[0], p[1] + offset)
        cand_nb = (p_nb[0]+moves[d][0], p_nb[1]+moves[d][1])
      
        if wh_cp[cand[0]][cand[1]] in {'[', ']'}:
            _, wh_cp = move2(d, cand, wh_cp)

        if wh_cp[cand_nb[0]][cand_nb[1]] in {'[', ']'}:
            _, wh_cp = move2(d, cand_nb, wh_cp)

        if wh_cp[cand[0]][cand[1]] == '.':
            wh_cp[cand[0]][cand[1]] = wh_cp[p[0]][p[1]]
            wh_cp[p[0]][p[1]] = '.'
            p_new1 = cand
        else :
            p_new1 = p

        if wh_cp[cand_nb[0]][cand_nb[1]] == '.':
            wh_cp[cand_nb[0]][cand_nb[1]] = wh_cp[p_nb[0]][p_nb[1]]
            wh_cp[p_nb[0]][p_nb[1]] = '.'
            p_new2 = cand_nb
        else :
            p_new2 = p_nb
       
        if p_new1[0] != p_new2[0]:
            return p, wh
        elif p[0] != p_new1[0]:
            return p_new1, wh_cp
    return p, wh

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    # data = aoc.get_input('input3.txt')
    
    robi, wh, instr = parsing(data)

    # Part I    
    
    for i in instr:
        robi = move(i, robi, wh)
    
    ans1 = sum_gps(wh)

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    robi, wh, instr = parsing2(data)

    for i in instr:
        robi, wh = move2(i, robi, wh)

    ans2 = sum_gps2(wh)
    
    print(f'Answer to part 2: {ans2}')
