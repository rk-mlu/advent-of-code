""" Advent of Code 2025 -- Day 6 -- """
year = 2025
day = 6         # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    nums = []

    for line in lines[:-1]:
        nums.append(np.array([int(n) for n in line.split()], dtype=int))

    line = lines[-1]
    ops = line.split()

    return nums, ops, lines


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input0.txt')
    
    nums, ops, lines = parsing(data)

    # Part I    
    
    ans1 = 0
    
    num_add = np.zeros(len(ops), dtype=int)
    num_mul = np.ones(len(ops), dtype=int)

    for num in nums:
        num_add += num
        num_mul *= num

    for j, o in enumerate(ops):
        if o == '+':
            ans1 += num_add[j]
        else :
            ans1 += num_mul[j]

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0

    # print(lines)
    num_col = len(lines[0])
    num_rows = len(nums)
    
    for n in range(num_col):
        if lines[-1][n] != ' ':
            # next group of numbers
            o = lines[-1][n]
            if o == '+':
                res = 0
            elif o == '*':
                res = 1
        
        # parse number 
        m = 0
        for j in range(num_rows):
            if lines[j][n] != ' ':
                m = m*10 + int(lines[j][n])

        if o == '+':
            res += m
        elif m != 0 :
            res *= m

        if m == 0 or n == num_col-1:
            # empty colunm or end of data
            # print(res)
            ans2 += res
    
    print(f'Answer to part 2: {ans2}')
