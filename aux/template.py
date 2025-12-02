""" Advent of Code 2025 -- Day X -- """
year = 2025
day = X         # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    return lines

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input0.txt')
    
    lines = parsing(data)

    # Part I    

    ans1 = 0

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    
    print(f'Answer to part 2: {ans2}')
