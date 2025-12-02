""" Advent of Code 2025 -- Day 01 -- """
year = 2025
day = 1     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    return lines

if __name__ == '__main__':
    # data = aoc.dl_data(day, year, 'input0.txt')                                  
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    lines = parsing(data)


    # Part I    
    ans1 = 0
    value = 50
    
    for line in lines:
        if line[0] == 'R':
            deg = int(line[1:])
            value = (value + deg) % 100
        if line[0] == 'L':
            deg = int(line[1:])
            value = (value - deg) % 100
        
        if value == 0:
            ans1 += 1

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    value = 50
    
    for line in lines:
        deg = int(line[1:])

        if line[0] == 'R':
            pre_value = value + deg
            n, value = divmod(pre_value, 100)
            ans2 += n          
            print(line, pre_value, value, ans2)

        if line[0] == 'L':
            pre_value = value - deg
            n, r = divmod(pre_value, 100)
            ans2 -= n
            if r == 0:
                ans2 += 1

            if value == 0 and n != 0:
                ans2 -= 1

            value = (value - deg) % 100
            print(line, pre_value, value, ans2)
        
    print(f'Answer to part 2: {ans2}')
