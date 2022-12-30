""" Advent of Code 2022 -- Day 24 -- """

import aoc
import numpy as np

class Blizzard:
    def __init__(self, pos, d, borders):
        self.pos = pos
        self.border = borders
        if d == '>':
            self.d = (0, 1)
        if d == '<':
            self.d = (0, -1)
        if d == 'v':
            self.d = (1, 0)
        if d == '^':
            self.d = (-1, 0)

    def move(self):
        new_pos = (self.pos[0] + self.d[0], self.pos[1] + self.d[1])
        # wrap around at border
        if new_pos[0] == 0:
            new_pos = (self.border[0]-2, self.pos[1] + self.d[1])
        if new_pos[0] == self.border[0]-1:
            new_pos = (1, self.pos[1] + self.d[1])
        if new_pos[1] == 0:
            new_pos = (self.pos[0] + self.d[0], self.border[1]-2)
        if new_pos[1] == self.border[1]-1:
            new_pos = (self.pos[0] + self.d[0], 1)

        self.pos = new_pos

class Expedition:
    def __init__(self, pos, mi):
        self.pos = pos
        self.mi = mi
        self.hist = [] 

    def list_moves(self, valley):
        row, col = valley.shape

        moves = []
        if valley[self.pos] == 0:
            # waiting
            moves.append((self.pos[0], self.pos[1]))
        if valley[self.pos[0]-1, self.pos[1]] == 0:
            # move north
            moves.append((self.pos[0]-1, self.pos[1]))
        if self.pos != (row-1, col-2):
            if valley[self.pos[0]+1, self.pos[1]] == 0:
                # move south
                moves.append((self.pos[0]+1, self.pos[1]))
        if valley[self.pos[0], self.pos[1]-1] == 0:
            # move west
            moves.append((self.pos[0], self.pos[1]-1))
        if valley[self.pos[0], self.pos[1]+1] == 0:
            # move east
            moves.append((self.pos[0], self.pos[1]+1))
        return moves
    
    def copy(self):
        pos_copy = (self.pos[0], self.pos[1])
        E = Expedition(pos_copy, self.mi)
        E.hist = self.hist.copy()
        return E

def get_valley(row, col):
    valley = np.zeros((row, col), dtype=int)
    # set borders
    valley[ 0,  :] = 1
    valley[-1,  :] = 1
    valley[ :,  0] = 1
    valley[ :, -1] = 1
    valley[ 0,  1] = 0
    valley[-1, -2] = 0

    return valley


def parsing(data):
    lines = data.splitlines()

    row = len(lines)
    col = len(lines[0])

    valley = get_valley(row, col)

    blizzards = set()

    b_chars = {'<', '>', '^', 'v'}
    
    for n, line in enumerate(lines):
        for m, d in enumerate(line):
            if d in b_chars:
                valley[n, m] = 1
                b = Blizzard((n,m), d, (row, col))
                blizzards.add(b)

    return blizzards, valley

def next_round(blizzards, valley, expeditions, goal):
    new_valley = get_valley(valley.shape[0], valley.shape[1])

    end = False

    for b in blizzards:
        b.move()
        new_valley[b.pos] = 1
    
    new_expeditions = set()
    for E in expeditions:
        moves = E.list_moves(new_valley)
        # print(moves)
        if len(moves) != 0:
            for k in range(len(moves)):
                E_new = Expedition(moves[k], E.mi + 1)
                E_new.hist = E.hist.copy()
                E_new.hist.append(moves[k])
                new_valley[E_new.pos] = -1
                new_expeditions.add(E_new)
                if E_new.pos == goal:
                    end = True

    new_expeditions.union(expeditions)
    
    return new_valley, new_expeditions, end

if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    # data = aoc.get_input('input3.txt')
    
    # Part I
    blizzards, valley = parsing(data)
    expeditions = set()
    E = Expedition((0,1), 0)
    expeditions.add(E)
    valley[0,1] = -1
    goal = (valley.shape[0]-1, valley.shape[1]-2)

    rounds = 400
    for r in range(rounds):
        print(f'Round {r+1}:')
        valley, expeditions, end = next_round(blizzards, valley, expeditions,
                goal)

        if end:
            break

    print(f'Part I: Expedition reached the goal in round {r+1}')

    # Part II
    blizzards, valley = parsing(data)
    
    start = (0,1)
    goal = (valley.shape[0]-1, valley.shape[1]-2)
    
    expeditions = set()
    E = Expedition(start, 0)
    expeditions.add(E)
    # valley[start] = -1

    tot_min = 0

    rounds = 400
    for r in range(rounds):
        print(f'Round {r+1}:')
        valley, expeditions, end = next_round(blizzards, valley, expeditions,
                goal)

        if end:
            tot_min += r + 1
            break

    expeditions = set()
    E = Expedition(goal, 0)
    expeditions.add(E)
    # valley[goal] = -1

    rounds = 400
    for r in range(rounds):
        print(f'Round {r+1}:')
        valley, expeditions, end = next_round(blizzards, valley, expeditions,
                start)

        if end:
            tot_min += r + 1
            break

    expeditions = set()
    E = Expedition(start, 0)
    expeditions.add(E)
    # valley[start] = -1

    rounds = 400
    for r in range(rounds):
        print(f'Round {r+1}:')
        valley, expeditions, end = next_round(blizzards, valley, expeditions,
                goal)

        if end:
            tot_min += r + 1
            break

    print(f'Part II: Expedition reached the goal in round {tot_min}')
