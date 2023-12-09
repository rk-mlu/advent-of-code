""" Advent of Code 2021 -- Day 04 -- """
year = 2021
day = 4     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    nums = [int(n) for n in lines[0].split(',')]
    
    boards = []
    
    m = len(lines[1:])//6

    for j in range(m):
        B = np.zeros((5,5), dtype=int)
        
        for i in range(5):
            row = [int(n) for n in lines[6*j + i + 2].split()]
            B[i,:] = np.array(row, dtype=int)
        
        boards.append(B)

    return nums, boards

def test_bingo(bb):
    for m in range(5):
        if np.all(np.logical_not(bb[m,:])) or np.all(np.logical_not(bb[:,m])):
            return True
    return False

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    nums, boards = parsing(data)
    

    boolboards = []
    for b in boards:
        boolboards.append(np.full((5,5), True))


    # Part I    
    no_bingo = True
    counter = 0
    while no_bingo and counter < len(nums):
        n = nums[counter]
        new_bb = []
        for b, bb in zip(boards, boolboards):
            bb_new = np.logical_and(bb, np.logical_not(b == n)) 
            new_bb.append(bb_new)
            if test_bingo(bb_new):
                no_bingo = False
                ans1 = np.sum(b[bb_new])*n 
                break
        boolboards = new_bb
        counter += 1
    
    print(f'Answer to part 1: {ans1}')

    # Part II
    boolboards = []
    for b in boards:
        boolboards.append(np.full((5,5), True))
    
    no_bingo = True
    num_bingo = 0
    counter = 0
    while no_bingo and counter < len(nums):
        n = nums[counter]
        new_bb = []
        for b, bb in zip(boards, boolboards):
            if test_bingo(bb):
                new_bb.append(bb)
                continue
            bb_new = np.logical_and(bb, np.logical_not(b == n)) 
            new_bb.append(bb_new)
            if test_bingo(bb_new):
                num_bingo += 1
            if num_bingo == len(boards):
                ans2 = np.sum(b[bb_new])*n 
                break
        boolboards = new_bb
        counter += 1
    
    print(f'Answer to part 2: {ans2}')
