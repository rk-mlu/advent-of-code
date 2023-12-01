""" Advent of Code 2023 -- Day 01 -- """

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def find_digits(line):
    digit1 = None
    digit2 = None
    for c in line:
        if c.isnumeric():
            if digit1 is None:
                digit1 = int(c)
            digit2 = int(c)
    return digit1, digit2

if __name__ == '__main__':
    
    # Part I    
    data = aoc.get_input('input1.txt')                                  
    
    summe = 0

    for line in data.splitlines():
        d1, d2 = find_digits(line)
        summe += d1*10 + d2
    
    ans1 = summe
    print(f'Answer to part 1" {ans1}')

    # Part II
    # data = aoc.get_input('input2.txt')
    
    word2num =[('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'),
            ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'),
            ('nine', '9'), ('zero','0')]

    ans2 = 0
    for line in data.splitlines():
        for (w,d) in word2num:
            line = line.replace(w,w+d+w)
        d1, d2 = find_digits(line)
        ans2 += d1*10 + d2

    print(f'Answer to part 2" {ans2}')
