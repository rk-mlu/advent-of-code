""" Advent of Code 2022 -- Day 09 -- """

import aoc
import numpy as np

class Rope:
    def __init__(self):
        self.head = np.zeros(2)
        self.tail = np.zeros(2)
        self.posH = {np.zeros(2)}
        self.posT = {np.zeros(2)}
    
    def move(self, line):
        word = line.split()
        
        num = int(word[1])
        
        for i in range(num):
            self.move_H(word[0])
        
    def move_H(self, d):
        directions = {}
        directions['R'] = np.array([1,0])
        directions['L'] = np.array([-1,0])
        directions['U'] = np.array([0, 1])
        directions['D'] = np.array([0,-1])

        self.head += directions[d]
    
    def __str__(self):
        s = f'H: {self.head}  T: {self.tail}'
        return s


if __name__ == '__main__':                                                      
    R = Rope()

    # data = aoc.get_input('input.txt')
    data = aoc.get_input('input2.txt')
    
    for line in data.splitlines():
        R.move(line)
        print(R)
        print(R.posH)
