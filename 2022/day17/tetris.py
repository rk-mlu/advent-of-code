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
        if self.type == 1:
            s = np.sum(chamber[self.h+1, self.pos:self.pos+3])
            s += chamber[self.h, self.pos+1]
            s += chamber[self.h+2, self.pos+1]
        if self.type == 2:
            s = np.sum(chamber[self.h, self.pos:self.pos+3])
            s += np.sum(chamber[self.h+1:self.h+3, self.pos+2])
        if self.type == 3:
            s = np.sum(chamber[self.h:self.h+4, self.pos])
        if self.type == 4:
            s = np.sum(chamber[self.h:self.h+2, self.pos:self.pos+2])
        return s
    
    def wind(self, d, chamber):
        if d == '<':
            self.pos -= 1
            if self.landed(chamber) != 0:
                self.pos += 1
        elif d == '>':
            self.pos += 1
            if self.landed(chamber) != 0:
                self.pos -= 1
        else: 
            print('parsing error!')

    def fall(self, chamber):
        self.h -= 1
        if self.landed(chamber) > 0:
            self.h += 1
            self.moving = False
    
    def rest(self, chamber, t, it):
        if self.type == 0:
            chamber[self.h, self.pos:self.pos+4] = 2
        if self.type == 1:
            chamber[self.h+1, self.pos:self.pos+3] = 2
            chamber[self.h, self.pos+1] = 2
            chamber[self.h+2, self.pos+1] = 2
            # if self.pos == 3 and it == 46:
            #     print(t+1, it)               
                
        if self.type == 2:
            chamber[self.h, self.pos:self.pos+3]   = 2
            chamber[self.h+1:self.h+3, self.pos+2] = 2
        if self.type == 3:
            chamber[self.h:self.h+4, self.pos] = 2
        if self.type == 4:
            chamber[self.h:self.h+2, self.pos:self.pos+2] = 2

        return chamber

def new_height(chamber, h = 0):
    new_height = h

    while np.sum(chamber[new_height+1,1:-1]) != 0:
        new_height += 1

    return new_height

def next_rock(t, h, it, chamber, gas):
    p = len(gas) - 1
    rock = Rock(t % 5, h)

    while rock.moving:
        rock.wind(gas[it], chamber)
        it = (it + 1)%p
        rock.fall(chamber)
    new_chamber = rock.rest(chamber, t, it)

    return it, new_chamber, rock

def comp_height(num_rocks, gas, h=0, it=0, chamber=None):
    if chamber is None:
        chamber = np.zeros((4*num_rocks, 9), dtype=int)
        chamber[0, :] =  1
        chamber[:, 0] = -1
        chamber[:,-1] = -1
    
    cycl = []
    for t in range(num_rocks):
        it, chamber, rock = next_rock(t, h, it, chamber, gas)
        h = new_height(chamber, h)
        if t % 5 == 1 and rock.pos == 3:
            # to detect cycles
            cycl.append(it)

    return h, it, chamber, cycl

def det_cycl_length(num_rocks, gas, min_it):
    chamber = np.zeros((4*num_rocks, 9), dtype=int)
    chamber[0, :] =  1
    chamber[:, 0] = -1
    chamber[:,-1] = -1
    
    it = 0
    h = 0
    t_min = num_rocks + 1
    t_2 = 0

    for t in range(num_rocks):
        it, chamber, rock = next_rock(t, h, it, chamber, gas)
        h = new_height(chamber, h)
        if t % 5 == 1 and rock.pos == 3 and it == min_it:
            # to detect cycles
            if t_min != num_rocks + 1:
                t_2 = t
                break
            else :
                t_min = min(t_min, t)


    return t_min, t_2 - t_min 

if __name__ == '__main__':
    gas = aoc.get_input('input.txt')                                  
    # gas = aoc.get_input('input2.txt')
    p = len(gas) - 1
    
    # Part I    
    num_rocks = 2022
    h, it, chamber, cycl = comp_height(num_rocks, gas)

    # print(chamber[::-1,:]) 
    print(f'Part I: The height of the tower with {num_rocks} rocks is {h}')

    # Part II
    
    total_rocks = 10**12 

    ## The number of total rocks is too large to solve the problem in the same
    ## way as part I.

    # However, after some time the tower becomes periodic.
    # Tasks:
    # 1) Determine time until the tower becomes periodic and length of period
    # 2) Determine height of tower during one period
    # 3) Determine number of remaining rocks to have in sum total_rocks

    # Detect start of cycle by searching for repetitions
    
    num_rocks = 20000
    
    h, it, chamber, cycl = comp_height(num_rocks, gas)

    values_it = {}

    for m in cycl:
        if m not in values_it.keys():
            values_it[m] = 1
        else :
            values_it[m] += 1
    
    # minimum value of _it_ that rock of type 1 repeats in pos == 3.
    min_it = np.amin(np.array(list(values_it.keys())))
    t_min, cycl_len = det_cycl_length(num_rocks, gas, min_it)

    num_cycles = (total_rocks - t_min - 1)//cycl_len
    remain_rocks = total_rocks - t_min - 1 - num_cycles*cycl_len

    num_rocks = t_min + 1
    h_1, it, chamber, cycl = comp_height(num_rocks, gas)
    
    num_rocks = t_min + cycl_len + 1 
    h_2, it, chamber, cycl = comp_height(num_rocks, gas)

    num_rocks = t_min + cycl_len + remain_rocks + 1
    h_3, it, chamber, cycl = comp_height(num_rocks, gas)
    
    total_height = h_1 + (h_2-h_1)*num_cycles + (h_3-h_2)
    print(f'Part II: The height of the tower with {total_rocks} rocks is {total_height}')
