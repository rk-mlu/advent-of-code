""" Advent of Code 2022 -- Day 10 -- """

import aoc
import numpy as np

class Register:
    def __init__(self):
        self.cycle = 0
        self.X = 1
        self.bounds = [20, 60, 100, 140, 180, 220]
        self.sigstr = []
        self.crt = ""

    def __str__(self):
        s = f'{sum(self.sigstr)}'
        return s

    def process(self, line):
        if line == 'noop':
            self.cycle += 1
            self.status()
        else :
            word = line.split()
            self.cycle += 1
            self.status()
            self.cycle += 1
            self.status()
            self.X += int(word[-1])
    
    def status(self):
        self.drawpixel()
        if self.cycle in self.bounds:
            self.strength()

    def strength(self):
        return self.sigstr.append(self.X*self.cycle)
    
    def drawpixel(self):
        if np.abs((self.cycle - 1) % 40 - self.X) <= 1:
            self.crt += '#'
        else :
            self.crt += '.'

        if (self.cycle) % 40 == 0:
            self.crt += '\n'

if __name__ == '__main__':
    A = Register()
    data = aoc.get_input('input.txt')
    # data = aoc.get_input('input2.txt')
     
    # Part I
    for line in data.splitlines():
       A.process(line)
    
    print(A)           
    print(A.crt)           
