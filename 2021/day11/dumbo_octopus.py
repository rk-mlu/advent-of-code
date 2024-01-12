""" Advent of Code 2021 -- Day 11 -- """
year = 2021
day = 11     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
from itertools import product

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    M = len(lines)
    N = len(lines[0])

    energy = np.zeros((M+2,N+2), dtype=int)

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            energy[i+1,j+1] = int(c)

    return energy

def do_step(energy):
    
    energy[1:-1,1:-1] += 1
    
    ind = np.argwhere(energy[1:-1, 1:-1] > 9)
    
    flashes = len(ind)

    while len(ind) > 0:
        energy[ind[:,0]+1, ind[:,1]+1] = -9
        for d1, d2 in product([0,1,2], [0,1,2]):
            energy[ind[:,0]+d1, ind[:,1]+d2] += 1 
        ind = np.argwhere(energy[1:-1, 1:-1] > 9)
        f = len(ind)
        flashes += f

    energy[1:-1, 1:-1] = np.where(energy[1:-1, 1:-1] >= 0, energy[1:-1,1:-1], 0)

    return energy, flashes

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    energy = parsing(data)

    # Part I    
   
    num_steps = 100
    ans1 = 0

    for j in range(num_steps):
        energy, f = do_step(energy)
        ans1 += f

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    energy = parsing(data)
    
    ans2 = 0
    f = 0
    
    M, N = energy.shape

    while f != (N-2)*(M-2):
        ans2 += 1
        energy, f = do_step(energy)

    print(f'Answer to part 2: {ans2}')
