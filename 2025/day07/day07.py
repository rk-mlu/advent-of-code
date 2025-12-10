""" Advent of Code 2025 -- Day 07 -- """
year = 2025
day = 7         # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    pos_S = lines[0].index('S')
    
    N = len(lines)
    M = len(lines[0])

    manif = np.zeros((N,M), dtype=int)

    for n, line in enumerate(lines[1:], start=1):
        for m, c in enumerate(line):
            if c == '^':
                manif[n,m] = 1
           

    return manif, pos_S

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input0.txt')
    
    manif, pos_S = parsing(data)
    

    # Part I    

    ans1 = 0

    N, M = manif.shape
    
    todo = set()
    todo.add(pos_S)
    
    splits = []

    for n in range(N-1):
        todo_new = set()
        num_splits = 0
        while len(todo) > 0:
            j = todo.pop()
            if manif[n+1,j]:
                todo_new.add(j-1)
                todo_new.add(j+1)
                num_splits += 1
            else :
                todo_new.add(j)
        todo = todo_new
        if num_splits:
            splits.append(num_splits)

    ans1 = sum(splits)
    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    
    todo = set()
    todo.add(pos_S)
    path = np.zeros_like(manif)
    path[0,pos_S] = 1
    
    for n in range(N-1):
        todo_new = set()
        while len(todo) > 0:
            j = todo.pop()
            if manif[n+1,j]:
                path[n+1, j-1] += path[n, j]
                todo_new.add(j-1)
                path[n+1, j+1] += path[n, j]
                todo_new.add(j+1)
            else :
                path[n+1, j] += path[n, j]
                todo_new.add(j)
        todo = todo_new
    
    ans2 = np.sum(path[-1,:])
    print(f'Answer to part 2: {ans2}')
