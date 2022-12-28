""" Advent of Code 2022 -- Day 23 -- """

import aoc
import numpy as np
import matplotlib.pyplot as plt

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Elf:
    def __init__(self, pos):
        self.pos = pos
        self.new_pos = None

    def propose(self, r, garden):
        i = self.pos[0]
        j = self.pos[1]
        adjacent = garden[i-1:i+2, j-1:j+2]
        # print(adjacent)
        if np.sum(np.sum(adjacent)) != 1:
            n = 0
            while n < 4:
                d = directions[(r+n) % 4]
                nb = adjacent[(1+d[0]-abs(d[1])):(2+d[0]+2*abs(d[1])),
                        (1+d[1]-abs(d[0])):(2+d[1]+2*abs(d[0]))]
                # print(n, nb)
                if np.sum(nb) == 0:
                    self.new_pos = (i+d[0], j+d[1])
                    break
                n += 1
        if self.pos is None:
            self.new_pos = self.pos


def parsing(data):
    lines = data.splitlines()

    row = len(lines)
    col = len(lines[0])
    
    elves = set()
    garden = np.zeros((row+2, col+2), dtype=int)
    
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                garden[i+1, j+1] = 1
                elves.add(Elf((i+1, j+1)))

    return garden, elves

def garden2str(garden):
    row, col = garden.shape

    s = ''
    for i in range(row):
        for j in range(col):
            if garden[i,j] == 0:
                s += '.'
            else :
                s += '#'
        s += '\n'

    return s

def next_round(r, garden, elves):
    # compute new proposed position for each elf
    next_pos = set()
    double_pos = set()

    for elf in elves:
        elf.propose(r, garden)
        if elf.new_pos in next_pos:
            # flag position that occure more than once
            double_pos.add(elf.new_pos)
        else :
            next_pos.add(elf.new_pos)

    M = True 
    if next_pos == {None}:
        M = False
    
    new_garden = np.zeros_like(garden)
    new_elves = set()
    for elf in elves:
        # do not move if more than one elf go to same field
        if elf.new_pos in double_pos:
            elf.new_pos = elf.pos
        new_elves.add(Elf(elf.new_pos))
        new_garden[elf.new_pos] = 1

    return new_garden, new_elves, M

if __name__ == '__main__':
    # data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    data = aoc.get_input('input3.txt')
    garden, elves = parsing(data)
    
    fig, ax = plt.subplots()
    ax.matshow(garden)

    print(garden2str(garden))
    # Part I    
    rounds = 10
    for r in range(rounds):
        garden, elves, mov = next_round(r, garden, elves)
        if mov == False:
            break
        print(f'\nRound {r+1}:')
        print(garden2str(garden))
        
        ax.clear()
        ax.matshow(garden)
        ax.set_title(f'Round {r+1}')
        plt.pause(0.5)
        


    # plt.matshow(garden)
    # plt.show()
    
    # Part II
