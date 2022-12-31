""" Advent of Code 2022 -- Day 14 -- """

import aoc
import numpy as np

class Sand:
    def __init__(self, start):
        self.pos = start
        self.moving = True
        self.abyss = False
        self.blocked = False
    
    def move(self, cave):
        row, col = cave.shape
        if self.pos[0] == row - 1:
            self.moving = False
            self.abyss = True
        elif cave[self.pos[0]+1,self.pos[1]] == 0:
            self.pos = (self.pos[0]+1, self.pos[1])
        elif cave[self.pos[0]+1,self.pos[1]-1] == 0: 
            self.pos = (self.pos[0]+1, self.pos[1]-1)
        elif cave[self.pos[0]+1,self.pos[1]+1] == 0: 
            self.pos = (self.pos[0]+1, self.pos[1]+1)
        else :
            self.moving = False

    def move2(self, cave):
        row, col = cave.shape
        if cave[self.pos[0]+1,self.pos[1]] == 0:
            self.pos = (self.pos[0]+1, self.pos[1])
        elif cave[self.pos[0]+1,self.pos[1]-1] == 0: 
            self.pos = (self.pos[0]+1, self.pos[1]-1)
        elif cave[self.pos[0]+1,self.pos[1]+1] == 0: 
            self.pos = (self.pos[0]+1, self.pos[1]+1)
        elif self.pos[0] == 0 :
            self.moving = False
            self.blocked = True            
        else :
            self.moving = False

def parsing(data):
    lines = data.splitlines()
    
    min_x = 500
    max_x = 500
    min_y = 0
    max_y = 0
     
    # parse data, get min/max for x and y coords
    coord_list = []
    for line in lines:
        coords = []
        lsplit = line.split(' -> ')
        for c in lsplit:
            x, y = c.split(',')
            x = int(x)
            y = int(y)
            coords.append((x,y))
            max_x = max(max_x, x)
            min_x = min(min_x, x)
            max_y = max(max_y, y)
            min_y = min(min_y, y)
        coord_list.append(coords)

    # print(coord_list)

    cave = np.zeros((max_y + 3, max_x - min_x + 3), dtype=int)
    cave[0, 500 - min_x + 1] = 1

    for coords in coord_list:
        for n in range(len(coords)-1):
            j1, i1 = coords[n]
            j2, i2 = coords[n+1]
            
            by1 = i1 - min_y
            by2 = i2 - min_y
            bx1 = j1 - min_x + 1
            bx2 = j2 - min_x + 1

            cave[min(by1, by2):max(by1, by2)+1, min(bx1, bx2):max(bx1, bx2)+1] = 1

    return cave

if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    # Part I
    cave = parsing(data)
    # print(cave)
    
    start = (0, np.argmax(cave[0,:]))
    abyss = False
    units = 0
    while not abyss:
        s = Sand(start)
        units += 1
        while s.moving:
            s.move(cave)
        cave[s.pos] = -1
        abyss = s.abyss
        # print(cave)
    print(f'Part I: Last unit of sand to come to rest is {units-1}')
    
    # Part II
    cave = parsing(data)
    start = (0, np.argmax(cave[0,:]))
    
    if 2*len(cave[:,0]) > len(cave[0,:]):
        cave_ext = np.zeros( (len(cave[:,0]), 2*len(cave[:,0])+4), dtype=int)
        shift = len(cave[:,0]) + 2 - start[1]
        cave_ext[:,shift:shift+len(cave[0,:])] = cave
    cave_ext[-1,:] = 1
    print(cave_ext)
    blocked = False
    units = 0

    while not blocked:
        s = Sand((0, start[1]+shift))
        units += 1
        while s.moving:
            s.move2(cave_ext)
        cave_ext[s.pos] = -1
        blocked = s.blocked
        # print(units)
    # print(cave_ext)
    print(f'Part II: Last unit of sand to come to rest is {units}')


