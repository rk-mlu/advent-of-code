""" Advent of Code 2022 -- Day 11 -- """

import aoc
import numpy as np

def parsing(data):

    hmap = np.zeros((41,101), dtype=int)

    for j, line in enumerate(data.splitlines()):
        for m, c in enumerate(line):
            if c == 'S':
                S = (j, m)

    return S, hmap



if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    # Part I
    S, hmap = parsing(data)
    print(S)
    
    # Part II
