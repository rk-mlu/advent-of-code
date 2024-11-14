""" Advent of Code 2020 -- Day 01 -- """
year = 2020
day = 1     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np
from itertools import combinations

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    return lines

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    lines = parsing(data)
    
    expenses = []
    for line in lines:
        expenses.append(int(line))

    # Part I    

    for num1, num2 in combinations(expenses, 2):
        if num1 + num2 == 2020:
            ans1 = num1*num2
            break

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    for num1, num2, num3 in combinations(expenses, 3):
        if num1 + num2 + num3 == 2020:
            ans2 = num1*num2*num3
            break
    
    print(f'Answer to part 2: {ans2}')
