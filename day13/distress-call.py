""" Advent of Code 2022 -- Day 13 -- """

import aoc
import ast
# import numpy as np

def parsing(data):
    packets = []

    for j, line in enumerate(data.splitlines()):

        if j % 3 == 2:
            # skip empty line
            continue

        if j % 3 == 0:
            pair = []
            
        pair.append(ast.literal_eval(line))

        if j % 2 == 1:
            packets.append(pair)

    return packets


if __name__ == '__main__':
    # data = aoc.get_input('input.txt')                                  
    data = aoc.get_input('input2.txt')
    
    # Part I    
    packets = parsing(data)
    print(packets)    

    # Part II
