""" Advent of Code 2022 -- Day 22 -- """

import aoc
import numpy as np

def parsing(data):
    lines = data.splitlines()

    # determine size of map
    row = len(lines) - 2
    
    col = 0
    for line in lines[:-2]:
        col = max(col, len(line))
    
    size = (row, col)

    # create board as numpy array
    # zero = empty tile, -1 = rock, 1 = open tile
    board = np.zeros(size, dtype=int)

    for i, line in enumerate(lines[:-2]):
        for j, c in enumerate(line):
            if c == '.':
                board[i,j] = 1
            if c == '#': 
                board[i,j] = -1
    
    # parse instructions
    cmd = lines[-1]
    instructions = [ ]
    s = ''
    for c in cmd:
        if c in {'R', 'L'}:
            instructions.append(int(s))
            s = ''
            instructions.append(c)
        else :
             s += c
    
    return board, size, instructions

class Walker:
    def __init__(self, board):
        self.pos = (0, np.argmax(board[0,:]))
        self.face = 0
        self.dir = (0,1) 
        
    def __str__(self):
        s = f'Pos = ({self.pos[0]}, {self.pos[1]})  with face {self.face}'
        return s

    def pswd(self):
        return 1000*(self.pos[0] + 1) + 4*(self.pos[1] + 1) + self.face
        
    def face2dir(self):
        if self.face == 0:
            self.dir = (0,1)
        elif self.face == 1:
            self.dir = (-1, 0)
        elif self.face == 2:
            self.dir = (0, -1)
        elif self.face == 3:
            self.dir = (1, 0)
    



if __name__ == '__main__':
    # data = aoc.get_input('input.txt')                                  
    data = aoc.get_input('input2.txt')
    
    # parse input
    board, size, path = parsing(data)
    print(board)
    print(path)

    # Part I    
    walker = Walker(board)
    print(walker)
    
    # Part II
