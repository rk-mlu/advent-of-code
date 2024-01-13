""" Advent of Code 2021 -- Day 13 -- """
year = 2021
day = 13     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    coords = []
    instr = []
    for line in lines:
        if ',' in line:
            x,y = line.split(',')
            coords.append((int(x), int(y)))
        elif 'fold' in line:
            w1, w2 = line.split('=')
            instr.append((w1[-1], int(w2)))

    return coords, instr

def prep_paper(coords):
    
    max_x = 0
    max_y = 0

    for x,y in coords:
        max_x = max(x, max_x)
        max_y = max(y, max_y)

    paper = np.zeros((max_y+1, max_x+1), dtype=int)

    for x,y in coords:
        paper[y,x] = 1 

    return paper

def fold_paper(instr, paper):
    M,N = paper.shape
    i = instr[1]

    if instr[0] == 'x':
        new_paper = paper[:, :i]
        for j in range(i+1,min(N, 2*i+1)):
            new_paper[:, 2*i-j] += paper[:, j]

    if instr[0] == 'y':
        new_paper = paper[:i, :]
        for j in range(i+1,min(M, 2*i+1)):
            new_paper[2*i-j, :] += paper[j, :]

    return new_paper

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    coords, instr = parsing(data)

    # Part I    
    
    paper = prep_paper(coords)
    paper = fold_paper(instr[0], paper)
    ans1 = np.count_nonzero(paper)

    print(f'Answer to part 1: {ans1}')

    # Part II

    paper = prep_paper(coords)

    for i in instr:
        paper = fold_paper(i, paper)

    print('Answer to part 2:')
    M, N = paper.shape
    
    for i in range(M):
        s = ''
        for j in range(N):
            if paper[i,j]:
                s += '#'
            else :
                s += '.'
        print(s)
