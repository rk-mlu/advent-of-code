""" Advent of Code 2021 -- Day 12 -- """
year = 2021
day = 12     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    V = set()
    E = set()

    for line in lines:
        n1, n2 = line.split('-')
        V.add(n1)
        V.add(n2)
        E.add((n1,n2))
        E.add((n2,n1))

    return V, E

def part1(V,E):
    v = 'start'

    visited = {v}

    def gen_path(v, visited):

        cands = [n2 for (n1,n2) in E if n1 == v]
        cands = [c for c in cands if not c in visited]

        num_path = 0
        for c in cands:
            if c == 'end':
                num_path += 1
            else :
                new_visited = visited.copy()
                if c.islower():
                    new_visited.add(c)
                num_path += gen_path(c, new_visited)
        return num_path
    num = gen_path(v, visited)
    return num

def part2(V,E):
    v = 'start'

    visited = {v}
    joker = True

    def gen_path(v, visited, joker):
        cands = [n2 for (n1,n2) in E if n1 == v and n2 != 'start']
        if not joker:
            cands = [c for c in cands if not c in visited]
        
        num_path = 0
        for c in cands:
            if c == 'end':
                num_path += 1
            else :
                new_visited = visited.copy()
                new_joker = joker
                if c.islower():
                    if c in visited:
                        new_joker = False
                    else :
                        new_visited.add(c)
                num_path += gen_path(c, new_visited, new_joker)
        return num_path

    num = gen_path(v, visited, joker)
    
    return num

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    V, E = parsing(data)

    # Part I    

    ans1 = part1(V, E)

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = part2(V, E)
    
    print(f'Answer to part 2: {ans2}')
