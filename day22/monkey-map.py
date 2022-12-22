""" Advent of Code 2022 -- Day 22 -- """

import aoc
# import numpy as np

def parsing(data):
    lines = data.splitlines()

    path = lines[-1]

    return path


if __name__ == '__main__':
    # data = aoc.get_input('input.txt')                                  
    data = aoc.get_input('input2.txt')
    
    path = parsing(data)
    print(path)

    # Part I    
    
    # Part II
