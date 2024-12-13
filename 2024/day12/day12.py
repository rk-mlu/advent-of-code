""" Advent of Code 2024 -- Day 12 -- """
year = 2024
day = 12     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    M = len(lines)
    N = len(lines[0])

    Map = []
    frame = (N+2)*'.'
    Map.append(frame)
    for line in lines:
        s = '.' + line + '.'
        Map.append(s)
    Map.append(frame)

    return Map, M, N

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    Map, M, N = parsing(data)

    # Part I    

    ans1 = 0
    visited = set()
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    gardens = []
    
    for m in range(1,M+1):
        for n in range(1,N+1):

            if (m,n) in visited:
                continue
            
            visited.add((m,n))
            
            plant = Map[m][n]
            garden = set()
            queue = [(m,n)]

            while len(queue) > 0:
                pos = queue.pop()
                garden.add((pos[0],pos[1]))
                visited.add((pos[0], pos[1]))

                for d in dirs:
                    x = pos[0] + d[0]
                    y = pos[1] + d[1]

                    if Map[x][y] != plant or (x,y) in garden:
                        continue
                    queue.append((x,y))

            gardens.append(garden)

    for g in gardens:
        perimeter = 0
        for tile in g:
            for d in dirs:
                x = tile[0] + d[0]
                y = tile[1] + d[1]

                if (x,y) not in g:
                    perimeter += 1
        print(len(g), perimeter)           


        ans1 += len(g)*perimeter

    
    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    
    for g in gardens:
        sides = 0
        for tile in g:
            nn = (tile[0]-1, tile[1])
            ne = (tile[0]-1, tile[1]+1)
            ee = (tile[0], tile[1]+1)
            se = (tile[0]+1, tile[1]+1)
            ss = (tile[0]+1, tile[1])
            sw = (tile[0]+1, tile[1]-1)
            ww = (tile[0], tile[1]-1)
            nw = (tile[0]-1, tile[1]-1)


            if (nn not in g):
                if (nw in g):
                    sides += 1
                elif ww not in g:
                    sides += 1

            if (ww not in g):
                if (sw in g):
                    sides += 1
                elif ss not in g:
                    sides += 1

            if (ss not in g):
                if (se in g):
                    sides += 1
                elif ee not in g:
                    sides += 1
            
            if (ee not in g):
                if (ne in g):
                    sides += 1
                elif nn not in g:
                    sides += 1
        print(len(g), sides)           


        ans2 += len(g)*sides
    
    print(f'Answer to part 2: {ans2}')
