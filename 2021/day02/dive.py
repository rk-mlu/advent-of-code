""" Advent of Code 2021 -- Day 02 -- """

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

if __name__ == '__main__':
    
    # Part I    
    data = aoc.get_input('input1.txt')                                  
    lines = data.splitlines()

    pos = [0, 0]

    for j, line in enumerate(lines):
        words = line.split()
        X = int(words[1])
        if words[0] == 'forward':
            pos[0] += X
        elif words[0] == 'down':
            pos[1] += X
        elif words[0] == 'up':
            pos[1] -= X
        else:
            print('error on input line', j+1)

        
    ans1 = pos[0]*pos[1]
    print(f'Answer to part 1" {ans1}')

    # Part II
    # data = aoc.get_input('input2.txt')

    pos = [0, 0, 0]

    for line in lines:
        words = line.split()
        X = int(words[1])
        if words[0] == 'down':
            pos[2] += X
        if words[0] == 'up':
            pos[2] -= X
        if words[0] == 'forward':
            pos[0] += X
            pos[1] += X*pos[2]
 
    ans2 = pos[0]*pos[1]
    print(f'Answer to part 2" {ans2}')
