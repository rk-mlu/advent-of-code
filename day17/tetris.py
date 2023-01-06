""" Advent of Code 2022 -- Day 17 -- """

import aoc
import numpy as np

class Rock:
    def __init__(self, t, h):
        self.pos = 3
        self.type = t
        self.h = h
        
    def landed(self, chamber):
        if self.type == 0:
            s = np.sum(chamber[self.h, self.pos:self.pos+4])
            return s


if __name__ == '__main__':
    # data = aoc.get_input('input.txt')                                  
    data = aoc.get_input('input2.txt')
    
    # Part I    
    chamber = np.zeros((10000, 9), dtype=int)
    chamber[0, :] =  1
    chamber[:, 0] = -1
    chamber[:,-1] = -1
    
    # Part II
