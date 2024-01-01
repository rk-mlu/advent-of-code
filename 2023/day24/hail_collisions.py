""" Advent of Code 2023 -- Day 24 -- """
year = 2023
day = 24        # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
from itertools import combinations
import sympy

def parsing(data, datatype=float):
    # parser for the input data; part II    
    lines = data.splitlines()
    
    M = len(lines)

    pos = np.zeros((M,3), dtype=datatype)
    vel = np.zeros((M,3), dtype=datatype)

    for j, line in enumerate(lines):
        poss, vels = line.split(' @ ')
        
        pos[j, :] = np.array([datatype(p) for p in poss.split(', ')])
        vel[j, :] = np.array([datatype(v) for v in vels.split(', ')])
    
    return pos, vel

def part1(pos, vel, lims):

    M, N = pos.shape
    
    ans1 = 0

    for i,j in combinations(range(M), 2):

        b = pos[i,:2] - pos[j,:2]
        
        A = np.zeros((2,2), dtype=float)
        
        A[:,0] = -vel[i,:2]
        A[:,1] = vel[j,:2]

        if np.linalg.det(A) == 0:
            # print(f'Pair {i},{j} is singular.')
            continue

        t = np.linalg.solve(A, b)
        # print(t)
        x = t[0]*vel[i,:2] + pos[i,:2]
        # print(x)
        
        if t[0] >= 0 and t[1] >= 0:
            x = t[0]*vel[i,:2] + pos[i,:2]
            if x[0] >= lims[0] and x[0] <= lims[1]:
                if x[1] >= lims[0] and x[1] <= lims[1]:
                    ans1 += 1

    return ans1

def part2(pos, vel):
    t1, t2, t3 = sympy.symbols('t1, t2, t3', integer=True)
    
    eqs = []
    for d in range(3):
        eqs.append( (t1-t3)*(t2*vel[1,d] + pos[1,d]) - (t1 - t2)*(t3*vel[2,d] +
            pos[2,d]) + (t3 - t2)*(t1*vel[0,d] + pos[0,d]))
        
    solutions = sympy.solve(eqs, t1, t2, t3, dict=True)
    # print(solutions)
    t_1 = solutions[1][t1]
    t_2 = solutions[1][t2]
    t_3 = solutions[1][t3]

    v = ((t_1*vel[0,:] + pos[0,:]) - (t_2*vel[1,:] + pos[1,:]))/(t_1 - t_2)
    # print(v)

    p = t_3*(vel[2,:] - v) + pos[2,:]
    # print(p)

    return p[0]+p[1]+p[2]

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    pos, vel = parsing(data)

    # Part I    
    # print(pos, vel)

    # ans1 = part1(pos, vel, (7., 27.))
    ans1 = part1(pos, vel, (200000000000000., 400000000000000.))

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    pos, vel = parsing(data, int)

    ans2 = part2(pos, vel)
    
    print(f'Answer to part 2: {ans2}')
