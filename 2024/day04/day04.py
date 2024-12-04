""" Advent of Code 2024 -- Day 04 -- """
year = 2024
day = 4     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    m = len(lines)
    n = len(lines[0])

    ext_lines = []
    dot_line = ['.']*(n+6)
    
    for j in range(3):
        ext_lines.append(dot_line)

    for line in lines:
        ext_line = 3*['.'] + [c for c in line] + 3*['.']
        ext_lines.append(ext_line)
    
    for j in range(3):
        ext_lines.append(dot_line)

    return m, n, ext_lines

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')

    m, n, lines = parsing(data)

    # Part I    

    ans1 = 0

    for i in range(3,m+3):
        for j in range(3,n+3):
            if lines[i][j] != 'X':
                continue
            else :
                if lines[i][j+1] == 'M' and lines[i][j+2] == 'A' and lines[i][j+3] == 'S':
                    ans1 += 1
                if lines[i][j-1] == 'M' and lines[i][j-2] == 'A' and lines[i][j-3] == 'S':
                    ans1 += 1
                if lines[i+1][j] == 'M' and lines[i+2][j] == 'A' and lines[i+3][j] == 'S':
                    ans1 += 1
                if lines[i-1][j] == 'M' and lines[i-2][j] == 'A' and lines[i-3][j] == 'S':
                    ans1 += 1
                if lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S':
                    ans1 += 1
                if lines[i-1][j-1] == 'M' and lines[i-2][j-2] == 'A' and lines[i-3][j-3] == 'S':
                    ans1 += 1
                if lines[i+1][j-1] == 'M' and lines[i+2][j-2] == 'A' and lines[i+3][j-3] == 'S':
                    ans1 += 1
                if lines[i-1][j+1] == 'M' and lines[i-2][j+2] == 'A' and lines[i-3][j+3] == 'S':
                    ans1 += 1


    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    
    for i in range(3,m+3):
        for j in range(3,n+3):
            if lines[i][j] != 'A':
                continue
            else :
                cond1 = lines[i+1][j+1] == 'M' and lines[i-1][j-1] == 'S'
                cond2 = lines[i+1][j+1] == 'S' and lines[i-1][j-1] == 'M'
                cond3 = lines[i+1][j-1] == 'S' and lines[i-1][j+1] == 'M'
                cond4 = lines[i+1][j-1] == 'M' and lines[i-1][j+1] == 'S'
                if (cond1 or cond2) and (cond3 or cond4):
                    ans2 += 1

    
    print(f'Answer to part 2: {ans2}')
