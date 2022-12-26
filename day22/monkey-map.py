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
    instructions.append(int(s))
    
    return board, size, instructions

class Walker:
    def __init__(self, board):
        self.pos = (0, np.argmax(board[0,:]))
        self.face = 0
        self.dir = (0,1)
        self.board = board
        self.row = board.shape[0]
        self.col = board.shape[1]
        self.s = ''
        
    def __str__(self):
        s = f'Pos = ({self.pos[0]}, {self.pos[1]})  with face {self.face}'
        return s

    def pswd(self):
        return 1000*(self.pos[0] + 1) + 4*(self.pos[1] + 1) + self.face
        
    def face2dir(self):
        if self.face == 0:
            self.dir = (0,1)
        elif self.face == 1:
            self.dir = (1, 0)
        elif self.face == 2:
            self.dir = (0, -1)
        elif self.face == 3:
            self.dir = (-1, 0)

    def move(self, inst):
        # move walker in part I
        if inst == 'R':
            self.face = (self.face + 1) % 4
            self.face2dir()
        if inst == 'L':
            self.face = (self.face - 1) % 4
            self.face2dir()
        if type(inst) is int:
            z = inst
            new_pos = (self.pos[0], self.pos[1])
            while z > 0:
                new_pos = ((new_pos[0] + self.dir[0]) % self.row,
                            (new_pos[1] + self.dir[1]) % self.col)
                if self.board[new_pos] == -1:
                    break
                else :
                    if self.board[new_pos] == 1:
                        self.pos = new_pos
                    z -= self.board[new_pos]

    def move2(self, inst):
        # move walker in part II
        # print(inst)
        self.face2dir()
        if inst == 'R':
            self.face = (self.face + 1) % 4
        if inst == 'L':
            self.face = (self.face - 1) % 4
        if type(inst) is int:
            new_pos = (self.pos[0], self.pos[1])
            new_face = self.face + 0
            for z in range(inst):
                new_pos = ((new_pos[0] + self.dir[0]) % self.row,
                            (new_pos[1] + self.dir[1]) % self.col)
                if self.board[new_pos] == 0:
                    new_pos, new_face = self.wrapping()
                if self.board[new_pos] == -1:
                    break
                if self.board[new_pos] == 1:
                    self.pos = new_pos
                    self.face = new_face
                    self.s += str(self.pos) + '\n'
                    self.face2dir()

    def wrapping(self):
        N = 50
        if self.pos[0] < N and self.pos[1] == N and self.face == 2:            
            # Leave 1 and enter 5
            new_pos = (3*N - self.pos[0] - 1, 0)
            new_face = 0
        if self.pos[0] < 3*N and self.pos[1] == 0 and self.face == 2:            
            # Leave 5 and enter 1
            new_pos = (3*N - self.pos[0] - 1, N)
            new_face = 0
        if self.pos[0] == 0 and self.pos[1] < 2*N and self.face == 3:            
            # Leave 1 and enter 4
            new_pos = (2*N + self.pos[1], 0)
            new_face = 0
        if self.pos[0] >= 3*N and self.pos[1] == 0 and self.face == 2:            
            # Leave 4 and enter 1
            new_pos = (0, self.pos[0]-2*N)
            new_face = 1
        if self.pos[0] == 0 and self.pos[1] >= 2*N and self.face == 3:            
            # Leave 2 and enter 4
            new_pos = (4*N - 1, self.pos[1] - 2*N)
            new_face = 3
        if self.pos[0] == 4*N - 1 and self.pos[1] < N and self.face == 1:            
            # Leave 4 and enter 2
            new_pos = (0, self.pos[1]+2*N)
            new_face = 1
        if self.pos[0] < N and self.pos[1] == 3*N - 1 and self.face == 0:            
            # Leave 2 and enter 6
            new_pos = (3*N - self.pos[0] - 1, 2*N - 1)
            new_face = 2
        if self.pos[0] >= 2*N and self.pos[1] == 2*N - 1 and self.face == 0:            
            # Leave 6 and enter 2
            new_pos = (3*N - self.pos[0] - 1, 3*N - 1)
            new_face = 2
        if self.pos[0] == N - 1 and self.pos[1] >= 2*N and self.face == 1:            
            # leave 2 and enter 3
            new_pos = (self.pos[1] - N, 2*N - 1)
            new_face = 2
        if self.pos[0] < 2*N and self.pos[1] == 2*N - 1 and self.face == 0:            
            # leave 3 and enter 2
            new_pos = (N - 1, self.pos[0] + N)
            new_face = 3
        if self.pos[0] >= N and self.pos[1] == N and self.face == 2:            
            # leave 3 and enter 5
            new_pos = (2*N, self.pos[0] - N)
            new_face = 1
        if self.pos[0] == 2*N and self.pos[1] < N and self.face == 3:            
            # leave 5 and enter 3
            new_pos = (N + self.pos[1], N)
            new_face = 0
        if self.pos[0] == 3*N - 1 and self.pos[1] >= N and self.face == 1:            
            # leave 6 and enter 4
            new_pos = (self.pos[1] + 2*N, N - 1)
            new_face = 2
        if self.pos[0] >= 3*N and self.pos[1] == N - 1 and self.face == 0:            
            # leave 4 and enter 6
            new_pos = (3*N - 1, self.pos[0] - 2*N)
            new_face = 3
        return new_pos, new_face


if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    # parse input
    board, size, path = parsing(data)
    # print(board)
    # print(size)
    # print(path)

    # Part I    
    walker = Walker(board)
    print(walker)
    for inst in path:
        walker.move(inst)
        # print(walker)
    print(f'Part I: The password is {walker.pswd()}')
    
    # Part II
    walker2 = Walker(board)
    print(walker2)
    # path2 = ['L', 1, 'R', 'R', 1]
    for inst in path:
        walker2.move2(inst)

    with open('pos_2.txt', 'w') as outf:
        outf.write(walker2.s)

    print(f'Part II: The password is {walker2.pswd()}')
