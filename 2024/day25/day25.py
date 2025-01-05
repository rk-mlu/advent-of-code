""" Advent of Code 2024 -- Day 25 -- """
year = 2024
day = 25     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    items = []
    new_item = []
    for line in lines:
        if len(line)>0:
            new_item.append(line)
        else :
            items.append(new_item)
            new_item = []
    items.append(new_item)

    return items

def test_lock(item):
    return item[0] == '#####' and item[-1] == '.....'
        
def test_key(item):
    return item[-1] == '#####' and item[0] == '.....'

def get_lock_heights(lock):
    heights = []
    for n in range(5):
        for m in range(6):
            if lock[m+1][n] == '.':
                heights.append(m)
                break
    return tuple(heights)

def get_pin_heights(lock):
    heights = []
    for n in range(5):
        for m in range(6):
            if lock[m+1][n] == '#':
                heights.append(5-m)
                break
    return tuple(heights)

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    items = parsing(data)

    locks = set()
    keys = set()

    for item in items:
        lock = test_lock(item)
        if lock:
            new_lock = get_lock_heights(item)
            locks.add(new_lock)
        if test_key(item):
            new_key = get_pin_heights(item)
            keys.add(new_key)

    print(f'number of locks: {len(locks)}')
    print(f'number of keys : {len(keys)}')

    # Part I    

    partition = dict()

    for m in range(5):
        partition[(m,5)] = keys.copy()
        for n in range(5):
            part = {key for key in keys if key[m] <= n}
            partition[(m,n)] = part

    ans1 = 0

    for lock in locks:
        fitting_keys = keys.copy()
        for m in range(5):
            fitting_keys = fitting_keys & partition[(m, 5-lock[m])]
        ans1 += len(fitting_keys)

    print(f'Answer to part 1: {ans1}')
