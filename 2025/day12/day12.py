""" Advent of Code 2025 -- Day 12 -- """
year = 2025
day = 12         # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    list_nums = []
    shapes = dict()

    for line in lines:
        if 'x' in line:
            size, nums = line.split(': ')
            s1, s2 = size.split('x')
            nums = [int(s1), int(s2)] + [int(n) for n in nums.split()]
            list_nums.append(tuple(nums))
        else :
            if ':' in line:
                key = line[:-1]
                shape = np.zeros((3,3), dtype=np.int16)
                i = 0
            elif len(line) > 0:
                for j, c in enumerate(line):
                    shape[i,j] = c == '#'
                i += 1
            else :
                shapes[key] = (shape, np.sum(np.sum(shape)))

    return shapes, list_nums

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input0.txt')
    
    shapes, nums = parsing(data)
    # print(nums)

    # Part I    
    
    ans1 = 0

    for rect in nums:
        size = rect[0]*rect[1]
        # print(rect[0], rect[1], size)

        min_size = 0
        for k in shapes.keys():
            min_size += shapes[k][1]*rect[int(k)+2]

        # print(min_size)   
        ans1 += min_size < size

    print(f'Answer to part 1: {ans1}')

