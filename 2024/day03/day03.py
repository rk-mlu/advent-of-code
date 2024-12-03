""" Advent of Code 2024 -- Day 03 -- """
year = 2024
day = 3     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    return lines

def comp_mul(s):
    pos = []
    j = s.find('mul(')

    res = 0

    while j != -1:
        pos.append(j)
        j = s.find('mul(', j+1)
    
    for j in pos:
        c = s.find(',',j+3)
        if c == -1:
            continue
        num1 = s[(j+4):c]
        if not num1.isnumeric():
            continue 
        num1 = int(num1)
        
        b = s.find(')',c)
        if b == -1:
            continue
        num2 = s[(c+1):b]
        if not num2.isnumeric():
            continue

        num2 = int(num2)

        res += num1*num2

    return res

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    lines = parsing(data)

    # Part I    

    ans1 = 0
    
    for line in lines:
        ans1 += comp_mul(line)
            
    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    
    s = 'do()' 
    
    for line in lines:
        s += line

    blocks = s.split("don't()")
    
    for block in blocks:
        k = block.find("do()")
        if k != -1:
            ans2 += comp_mul(block[k:])
    
    print(f'Answer to part 2: {ans2}')
