""" Advent of Code 2023 -- Day 02 -- """

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parse_game(line):
    split1 = line.split(':')
    subgs = split1[1].split(';')

    subgs_list = []
    for subg in subgs:
        col = subg.split(',')
        cols = [c.split() for c in col]
        
        red = 0
        green = 0
        blue = 0
        
        for (n, c) in cols:
            if c == 'red':
                red = int(n)
            if c == 'green':
                green = int(n)
            if c == 'blue':
                blue = int(n)
        subgs_list.append((red,green,blue))
    
    return subgs_list

if __name__ == '__main__':
    
    data = aoc.get_input('input1.txt')                                  
    lines = data.splitlines()

    # Part I    
    max_red = 12
    max_green = 13
    max_blue = 14

    ans1 = 0
    for i, line in enumerate(lines):
        subg_list = parse_game(line)

        possible = True
        for subg in subg_list:
            if subg[0] > max_red:
                possible = False
            if subg[1] > max_green:
                possible = False
            if subg[2] > max_blue:
                possible = False
        if possible:
            ans1 += i + 1  # add ID of game

    print(f'Answer to part 1" {ans1}')

    # Part II
    # data = aoc.get_input('input2.txt')
    
    ans2 = 0
    
    for game in lines:
        min_red = 0
        min_green = 0
        min_blue = 0
        
        subg_list = parse_game(game)

        for subg in subg_list:
            min_red = max(min_red, subg[0])
            min_green = max(min_green, subg[1])
            min_blue = max(min_blue, subg[2])
        
        power = min_red*min_green*min_blue
        
        ans2 += power

    print(f'Answer to part 2" {ans2}')
