""" Advent of Code 2024 -- Day XX -- """
year = 2025
day = 2     # set day!

import sys
sys.path.append('../../aux')
import aoc
from math import sqrt
# import numpy as np

def parsing(data):
    # parser for the input data    
    ranges = data.split(',')

    out = [rge.split('-') for rge in ranges]
    out = [ (int(s), int(e)) for s,e in out]

    return out

def is_invalid(ID):
    valid = True
    ID = str(ID)
    l = len(ID)

    if l % 2 == 0:
        mid = l//2
        left = ID[:mid]
        right = ID[mid:]
        if left == right:
            valid = False

    return not valid

def get_divisors(n):
    divisors = []
    
    for d in range(1, int(sqrt(n))+1):
        m, r = divmod(n, d)

        if r == 0:
            divisors.append(d)
            divisors.append(m)

    return divisors


def is_invalid2(ID):
    ID = str(ID)
    l = len(ID)

    divisors = get_divisors(l)

    for d in divisors:
        m = l//d
        if m == 1:
            continue
        
        start = ID[:d]
        # print(start)
        
        for j in range(1,m):
            s = ID[j*d:(j+1)*d]
            # print(s)

            if s != start:
                break
            elif j == m - 1:
                return True              

    return False

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input0.txt')
    
    ranges = parsing(data)

    # Part I    
    
    ans1 = 0

    for s,e in ranges:
        for ID in range(s, e+1):
            if is_invalid(ID):
                # print(ID)
                ans1 += ID

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0

    invalid_set = set()
    
    for s,e in ranges:
        print(s,e)
        for ID in range(s, e+1):
            if is_invalid2(ID):
                print(ID)
                invalid_set.add(ID)

    ans2 = sum([s for s in invalid_set])

    print(f'Answer to part 2: {ans2}')
