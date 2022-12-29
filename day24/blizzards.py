""" Advent of Code 2022 -- Day 24 -- """

import aoc
# import numpy as np

class Blizzard:
    def __init__(self, pos, d, borders):
        self.pos = pos
        self.borders = borders
        if d == '>':
            self.d = (0, 1)
        if d == '<':
            self.d = (0, -1)
        if d == 'v':
            self.d = (1, 0)
        if d == '^':
            self.d = (-1, 0)


def parsing(data):
    lines = data.splitlines()

    row = len(lines)
    col = len(lines[0])

    blizzards = set()

    b_chars = {'<', '>', '^', 'v'}
    
    for n, line in enumerate(lines):
        for m, c in enumerate(line):
            if c in b_chars:
                b = Blizzard((n,m), c, (row, col))
                blizzards.add(b)

    return blizzards

if __name__ == '__main__':
    # data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    data = aoc.get_input('input3.txt')
    
    # Part I
    blizzards = parsing(data)
    print(len(blizzards))
    
    
    # Part II
