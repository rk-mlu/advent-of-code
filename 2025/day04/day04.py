""" Advent of Code 2025 -- Day 4 -- """
year = 2025
day = 4         # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
from itertools import product

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    N = len(lines)
    M = len(lines[0])
    
    A = np.zeros((N+2, M+2), dtype=int)

    for n, line in enumerate(lines):
        for m, c in enumerate(line):
            if c == '@':
                A[n+1,m+1] = 1
    
    return A, N, M

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input0.txt')
    
    A, N, M = parsing(data)
    # print(A)
    
    # Part I    

    ans1 = 0
    
    for n in range(1,N+1):
        for m in range(1,M+1):
            if A[n,m] == 1 and np.sum(A[n-1:n+2,m-1:m+2]) < 5:
                ans1 += 1

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    removed = 1
    todo = [(n,m) for (n,m) in product(range(1,N+1), range(1, M+1))]

    while removed > 0:
        removed = 0
        A_new = A.copy()
        todo_new = []
        for n, m in todo:
            if A[n,m] == 1:
                if np.sum(A[n-1:n+2,m-1:m+2]) < 5:
                    removed += 1
                    A_new[n,m] = 0
                else :
                    todo_new.append((n,m))
        A = A_new
        todo = todo_new
        ans2 += removed
    
    print(f'Answer to part 2: {ans2}')
