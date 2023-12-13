""" Advent of Code 2023 -- Day 13 -- """
year = 2023
day = 13     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
from itertools import product

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    patterns = []
    pattern = []

    for line in lines:
        if len(line) == 0:
            patterns.append(np.array(pattern, dtype=int))
            pattern = []
            continue
        p_line = []
        for c in line:
            if c == '#':
                p_line.append(1)
            else :
                p_line.append(0)
        pattern.append(p_line)
    patterns.append(np.array(pattern, dtype=int))

    return patterns

def find_refl(pat, old_value = -1):
    M, N = pat.shape
    ans = 0 
    for c in range(N-1):
        lim = min(c, N-c-2)+1
        refl = True
        for l in range(lim):
            refl = refl and np.array_equal(pat[:,c-l], pat[:,c+l+1])
        if refl:
            ans = c + 1
            if ans != old_value:
                return ans

    for r in range(M-1):
        lim = min(r, M-r-2)+1
        refl = True
        for l in range(lim):
            refl = refl and np.array_equal(pat[r-l,:], pat[r+l+1,:])
        if refl:
            ans = 100*(r+1)
            if ans != old_value:
                return ans
    return ans


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    patterns = parsing(data)

    # Part I    
    
    ans1 = 0
    
    for pat in patterns:
        ans1 += find_refl(pat)

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    
    for pat in patterns:
        M, N = pat.shape
        old_ans = find_refl(pat)
        for i, j in product(range(M), range(N)):
            pat2 = pat.copy()
            pat2[i,j] = 1 - pat[i,j]
            new_ans = find_refl(pat2, old_ans)
            if new_ans != old_ans and new_ans !=0:
                ans2 += new_ans
                break
    
    print(f'Answer to part 2: {ans2}')
