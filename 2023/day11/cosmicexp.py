""" Advent of Code 2023 -- Day 11 -- """
year = 2023
day = 11     # set day!

from itertools import combinations
import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    N = len(lines)
    M = len(lines[0])

    cosmos = np.zeros((N,M), dtype=int)

    for j in range(N):
        for k in range(M):
            if lines[j][k] == '#':
                cosmos[j,k] = 1

    return cosmos

def expand(cosmos):
    N, M = cosmos.shape
    
    cosmos_exp = cosmos.copy()
    
    row_add = 0
    row_exps = []
    for j in range(N):
        if np.sum(cosmos[j,:]) == 0:
            # print(f'expanding row {j}')
            cosmos_exp = np.insert(cosmos_exp, j + row_add, 0, axis=0)
            row_exps.append(j)
            row_add += 1

    col_add = 0
    col_exps = []
    for k in range(M):
        if np.sum(cosmos[:,k]) == 0:
            # print(f'expanding col {k}')
            cosmos_exp = np.insert(cosmos_exp, k + col_add, 0, axis=1)
            col_exps.append(k)
            col_add += 1

    return cosmos_exp, row_exps, col_exps

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    cosmos = parsing(data)

    # Part I    
    
    cosmos_exp, r_list, c_list = expand(cosmos)
    N, M = cosmos_exp.shape

    galaxy_coord = np.nonzero(cosmos_exp)

    num_gal = len(galaxy_coord[0])
    
    ans1 = 0
    
    for (j1, j2) in combinations(range(num_gal),2):
        c1 = np.array([galaxy_coord[0][j1], galaxy_coord[1][j1]])
        c2 = np.array([galaxy_coord[0][j2], galaxy_coord[1][j2]])
        d = np.abs(c1[0] - c2[0]) + np.abs(c1[1] - c2[1])
        ans1 += d
        
    print(f'Answer to part 1: {ans1}')

    # Part II
    galaxy_coord2 = np.nonzero(cosmos)
    galaxy_coord2_exp = np.nonzero(cosmos) 
        
    for k in range(num_gal):
        for j in range(len(r_list)):
            if galaxy_coord2[0][k] > r_list[j]:
                galaxy_coord2_exp[0][k] += 10**6 - 1

    for k in range(num_gal):
        for j in range(len(c_list)):
            if galaxy_coord2[1][k] > c_list[j]:
                galaxy_coord2_exp[1][k] += 10**6 - 1
    
    ans2 = 0
    
    for (j1, j2) in combinations(range(num_gal),2):
        c1 = np.array([galaxy_coord2_exp[0][j1], galaxy_coord2_exp[1][j1]])
        c2 = np.array([galaxy_coord2_exp[0][j2], galaxy_coord2_exp[1][j2]])
        d = np.abs(c1[0] - c2[0]) + np.abs(c1[1] - c2[1])
        ans2 += d

    print(f'Answer to part 2: {ans2}')
