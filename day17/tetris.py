""" Advent of Code 2022 -- Day 17 -- """

import aoc
import numpy as np

class Rock:
    def __init__(self, t, h):
        self.type = t
        self.pos = 3
        self.h = h + 4
        self.moving = True
        
    def landed(self, chamber):
        if self.type == 0:
            s = np.sum(chamber[self.h, self.pos:self.pos+4])
            return s
        if self.type == 1:
            s = np.sum(chamber[self.h+1, self.pos:self.pos+3])
            s += chamber[self.h, self.pos+1]
            s += chamber[self.h+2, self.pos+1]
            return s
        if self.type == 2:
            s = np.sum(chamber[self.h, self.pos:self.pos+3])
            s += np.sum(chamber[self.h+1:self.h+3, self.pos+2])
            return s
        if self.type == 3:
            s = np.sum(chamber[self.h:self.h+4, self.pos])
            return s
        if self.type == 4:
            s = np.sum(chamber[self.h:self.h+2, self.pos:self.pos+2])
            return s
    
    def wind(self, d, chamber):
        if d == '<':
            self.pos -= 1
            if self.landed(chamber) != 0:
                self.pos += 1
        if d == '>':
            self.pos += 1
            if self.landed(chamber) != 0:
                self.pos -= 1

    def fall(self, chamber):
        self.h -= 1
        # print(self.landed(chamber))
        if self.landed(chamber) > 0:
            self.h += 1
            self.moving = False
    
    def rest(self, chamber):
        new_chamber = chamber.copy()
        if self.type == 0:
            new_chamber[self.h, self.pos:self.pos+4] = 2
        if self.type == 1:
            new_chamber[self.h+1, self.pos:self.pos+3] = 2
            new_chamber[self.h, self.pos+1] = 2
            new_chamber[self.h+2, self.pos+1] = 2
        if self.type == 2:
            new_chamber[self.h, self.pos:self.pos+3]   = 2
            new_chamber[self.h+1:self.h+3, self.pos+2] = 2
        if self.type == 3:
            new_chamber[self.h:self.h+4, self.pos] = 2
        if self.type == 4:
            new_chamber[self.h:self.h+2, self.pos:self.pos+2] = 2

        return new_chamber

def new_height(chamber, h = 0):
    new_height = h

    while np.sum(chamber[new_height+1,1:-1]) != 0:
        new_height += 1

    return new_height

def next_rock(t, h, it, chamber, gas):
    p = len(gas) - 1
    rock = Rock(t, h)

    while rock.moving:
        rock.wind(gas[it], chamber)
        it = (it + 1)%p
        rock.fall(chamber)
    new_chamber = rock.rest(chamber)

    return it, new_chamber



if __name__ == '__main__':
    gas = aoc.get_input('input.txt')                                  
    # gas = aoc.get_input('input2.txt')
    
    # Part I    
    num_rocks = 2022 

    chamber = np.zeros((2*num_rocks, 9), dtype=int)
    chamber[0, :] =  1
    chamber[:, 0] = -1
    chamber[:,-1] = -1

    h = 0
    it = 0

    for t in range(num_rocks):
        it, chamber = next_rock(t % 5, h, it, chamber, gas)
        h = new_height(chamber, h)

    # print(chamber[::-1,:]) 
    print(f'Part I: The height of the tower with {num_rocks} rocks is {h}')

    # Part II
    num_rocks = 10000

