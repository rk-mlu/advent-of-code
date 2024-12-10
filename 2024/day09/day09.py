""" Advent of Code 2024 -- Day 9 -- """
year = 2024
day = 9     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
from itertools import islice, pairwise

def comp_checksum(fs):
    N = len(fs)
    positions = np.arange(N, dtype=int)
    mask = fs != -1
    return np.dot(fs[mask], positions[mask])

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = "2333133121414131402"

    # Part I    
    
    if len(data) % 2 == 1:
        data += '0'

    max_len = sum([int(n) for n in data])

    fs = (-1)*np.ones(max_len, dtype=int)
    pt = 0

    for i, (b, c) in enumerate(islice(pairwise(data), 0, None, 2)):
        fs[pt:pt+int(b)] = i
        pt += int(b) + int(c)

    pt1 = 0
    pt2 = max_len -1

    while pt1 < pt2:
        if fs[pt1] != -1:
            pt1 += 1
        else :
            if fs[pt2] != -1:
                fs[pt1] = fs[pt2]
            pt2 -= 1

    ans1 = comp_checksum(fs[:pt2])

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    
    fs = (-1)*np.ones(max_len, dtype=int)
    blocks = []
    pt = 0

    for i, (b, c) in enumerate(islice(pairwise(data), 0, None, 2)):
        fs[pt:pt+int(b)] = i
        blocks.append(int(b))
        blocks.append(int(c))
        pt += int(b) + int(c)
    
    num_files = len(data)//2
    old_blocks = blocks.copy()

    for i in range(num_files-1, -1, -1):

        file_size = old_blocks[2*i]

        k = 0
        while k <= i and blocks[2*k+1] < file_size:
            k += 1

        if k <= i:
            new_start = sum(blocks[:2*k+1])
            old_start = sum(blocks[:2*i])
            fs[new_start:new_start+file_size] = fs[old_start:old_start+file_size]
            fs[old_start:old_start+file_size] = -1

            blocks[2*k+1] -= file_size
            blocks[2*k] += file_size
            blocks[2*i] -= file_size
            blocks[2*i+1] += file_size

    # print(fs)
    ans2 = comp_checksum(fs)
    
    print(f'Answer to part 2: {ans2}')
