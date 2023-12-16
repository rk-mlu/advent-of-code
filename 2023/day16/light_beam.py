""" Advent of Code 2023 -- Day 16 -- """
year = 2023
day = 16     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    return lines

def move(beam, lines):
    M = len(lines)
    N = len(lines[0])

    new_beams = []
    
    new_x = beam[0]
    new_y = beam[1]
    new_dir_x = beam[2]
    new_dir_y = beam[3]
    
    if lines[beam[0]][beam[1]] == '.':
        new_x += beam[2]
        new_y += beam[3]
        
        if new_x < M and new_x > -1 and new_y > -1 and new_y < N:
            new_beams.append((new_x, new_y, new_dir_x, new_dir_y))
    
    if lines[beam[0]][beam[1]] == '|':
        if beam[3] == 0:
            new_x += beam[2]
            if new_x < M and new_x > -1:
                new_beams.append((new_x, new_y, new_dir_x, new_dir_y))
        else :
            new_x1 = new_x + 1
            new_x2 = new_x - 1
            new_dir_x1 = 1
            new_dir_x2 = -1
            new_dir_y = 0
            if new_x1 < M and new_x1 > -1:
                new_beams.append((new_x1, new_y, new_dir_x1, new_dir_y))
            if new_x2 < M and new_x2 > -1:
                new_beams.append((new_x2, new_y, new_dir_x2, new_dir_y))
    
    if lines[beam[0]][beam[1]] == '-':
        if beam[2] == 0:
            new_y += beam[3]
            if new_y < N and new_y > -1:
                new_beams.append((new_x, new_y, new_dir_x, new_dir_y))
        else :
            new_y1 = new_y + 1
            new_y2 = new_y - 1
            new_dir_y1 = 1
            new_dir_y2 = -1
            new_dir_x = 0
            if new_y1 < N and new_y1 > -1:
                new_beams.append((new_x, new_y1, new_dir_x, new_dir_y1))
            if new_y2 < N and new_y2 > -1:
                new_beams.append((new_x, new_y2, new_dir_x, new_dir_y2))
    
    if lines[beam[0]][beam[1]] == '/':
        if beam[3] != 0:
            new_x -= beam[3]
            new_dir_x = (-1)*beam[3]
            new_dir_y = 0
        else :
            new_y -= beam[2]
            new_dir_y = (-1)*beam[2]
            new_dir_x = 0
        if new_x < M and new_x > -1 and new_y > -1 and new_y < N:
            new_beams.append((new_x, new_y, new_dir_x, new_dir_y))
    
    if lines[beam[0]][beam[1]] == '\\':
        if beam[3] != 0:
            new_x += beam[3]
            new_dir_x = beam[3]
            new_dir_y = 0
        else :
            new_y += beam[2]
            new_dir_y = beam[2]
            new_dir_x = 0
        if new_x < M and new_x > -1 and new_y > -1 and new_y < N:
            new_beams.append((new_x, new_y, new_dir_x, new_dir_y))

    return new_beams

def num_energized(start, lines):
    tiles = set()
    tiles.add(start)
    active = [start]

    while len(active) > 0:
        beam = active.pop()
        beams = move(beam, lines)
        for beam in beams:
            if beam not in tiles:
                tiles.add(beam)
                active = active + [beam]
    
    energized = set()
    for t in tiles:
        energized.add(t[:2])
    
    return len(energized)



if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    lines = parsing(data)

    # Part I    

    start = (0, 0, 0, 1)
    
    ans1 = num_energized(start, lines)

    print(f'Answer to part 1: {ans1}')

    # Part II

    ans2 = 0

    M = len(lines)
    N = len(lines[0])

    for i in range(M):
        start = (i, 0, 0, 1)
        ans2 = max(ans2, num_energized(start, lines))
        start = (i, N-1, 0, -1)
        ans2 = max(ans2, num_energized(start, lines))

    for j in range(N):
        start = (0, j, 1, 0)
        ans2 = max(ans2, num_energized(start, lines))
        start = (M-1, j, -1, 0)
        ans2 = max(ans2, num_energized(start, lines))
    
    print(f'Answer to part 2: {ans2}')
