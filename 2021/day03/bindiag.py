""" Advent of Code 2021 -- Day 03 -- """

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def filter_numbers(crit, lines):
    m = len(lines)
    n = len(lines[0])

    B = np.zeros((m,n), dtype=int)

    for i in range(m):
        for j in range(n):
            if lines[i][j] == '1':
                B[i,j] = 1
    valid = np.ones(m, dtype=int)
    
    col = 0
    while np.sum(valid) > 1:
        num = np.sum(valid)
        
        valid_rows = (valid == 1)

        if (-1)**crit * 2*np.sum(B[valid_rows, col]) - crit < (-1)**crit*num:
            # keep only 'crit'
            valid[valid_rows] = valid[valid_rows]*B[valid_rows, col]
        else :
            valid[valid_rows] = valid[valid_rows]*(1 - B[valid_rows, col])
        
    
        col += 1

    return B[valid==1, :][0]
    

if __name__ == '__main__':
    
    # Part I    
    data = aoc.get_input('input1.txt')                                  
    # data = aoc.get_input('input2.txt')                                  
    lines = data.splitlines()
    
    n = len(lines[0])
    counters = np.zeros(n)
    
    for line in lines:
        for j, c in enumerate(line):
            counters[j] += int(c)
    
    gamma = 0
    epsilon = 0
    for j, val in enumerate(counters):
        if val > len(lines)//2:
            gamma += 2**(n-j-1)
        else:
            epsilon += 2**(n-j-1)
    
    ans1 = gamma*epsilon
    print(f'Answer to part 1: {ans1}')

    # Part II
    # data = aoc.get_input('input2.txt')
    
    O2 = filter_numbers(1, lines)
    CO2 = filter_numbers(0, lines)
   
    o2rat = 0
    co2rat = 0
    for j, (bO2, bCO2) in enumerate(zip(O2, CO2)):
        o2rat += bO2*2**(n-j-1)
        co2rat += bCO2*2**(n-j-1)
    
    ans2 = o2rat* co2rat
    print(f'Answer to part 2: {ans2}')
