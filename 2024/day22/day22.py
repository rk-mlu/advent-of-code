""" Advent of Code 2024 -- Day 22 -- """
year = 2024
day = 22     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
from itertools import islice

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    seeds = np.array([int(n) for n in lines], dtype=np.uint64)
    return seeds

def monkey_rng(seeds):
    lshift1 = 6
    lshift2 = 11
    rshift = 5
    prune_mod = 16777216
    while True:
        yield seeds
        # step 1
        mul64 = np.left_shift(seeds, lshift1, dtype=np.uint64)
        np.bitwise_xor(seeds, mul64, out=seeds)
        np.mod(seeds, prune_mod, out=seeds)
        # step 2
        div32 = np.right_shift(seeds, rshift, dtype=np.uint64)  
        np.bitwise_xor(seeds, div32, out=seeds)
        np.mod(seeds, prune_mod, out=seeds)
        # step 3
        mul2048 = np.left_shift(seeds, lshift2, dtype=np.uint64)
        np.bitwise_xor(seeds, mul2048, out=seeds)
        np.mod(seeds, prune_mod, out=seeds)
        # print(seeds)


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    seeds = parsing(data)
    M = len(seeds)

    # Part I    
    N = 2001
    seeds1 = seeds.copy()
    for prnums in islice(monkey_rng(seeds1), N):
        pass

    ans1 = np.sum(seeds1)
    print(f'Answer to part 1: {ans1}')

    # Part II
    prices = np.mod(seeds.copy(), 10, dtype=np.uint64)
    diff = np.zeros((M,4), dtype=np.int64)
    
    mem = dict()
    c = 0

    for prnums in islice(monkey_rng(seeds), 1, N):
        # diff_new = np.zeros((M,4), dtype=np.int64)
        # diff_new[:,:3] = diff[:,1:]
        # print(diff_new)
        diff = np.roll(diff, -1, axis=1)
        new_prices = np.mod(prnums, 10, dtype=np.uint64)
        diff[:,3] = new_prices - prices
        prices = new_prices
        if c < 4:
            c += 1
        else :
            for j in range(M):
                tup = tuple(diff[j,:])
                pref_prices = mem.get(tup, (-1)*np.ones(M, dtype=np.int64))
                if pref_prices[j] == -1:
                    pref_prices[j] = prices[j]
                mem[tup] = pref_prices
                
    ans2 = 0
    best_tup = None
    for tup, pr in mem.items():
        s = np.sum(pr[pr> -1])
        if ans2 < s:
            best_tup = tup
            ans2 = s
    
    print('Best changes:', best_tup)
    
    
    print(f'Answer to part 2: {ans2}')
