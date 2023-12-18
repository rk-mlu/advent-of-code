""" Advent of Code 2021 -- Day 08 -- """
year = 2021
day = 8     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np
from collections import defaultdict

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    in_sig = []
    out_sig = []
    for line in lines:
        ins, outs = line.split(' | ')
        in_sig.append(ins.split())
        out_sig.append(outs.split())

    return in_sig, out_sig

def decode_sig(s, cond):

    if len(s) == 2:
        return 1
    if len(s) == 3:
        return 7
    if len(s) == 7:
        return 8
    if len(s) == 4:
        return 4
    chars = set(s)
    if len(s) == 5:
        for k in [2, 3, 5]:
            if len(chars.intersection(cond[k])) == 5:
                return k

    if len(s) == 6:
        for k in [0, 6, 9]:
            if len(chars.intersection(cond[k])) == 6:
                return k
    



if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    ins, outs = parsing(data)
    
    # Part I    

    ans1 = 0

    for out in outs:
        for s in out:
            if len(s) in [2, 3, 4, 7]:
                ans1 += 1

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0

    for in_s, out in zip(ins, outs):
        decode = defaultdict(set)

        for sig in in_s + out:
            if len(sig) == 2:
                decode[1] = set(sig)
            if len(sig) == 3:
                decode[7] = set(sig)
            if len(sig) == 4:
                decode[4] = set(sig)
            if len(sig) == 7:
                decode[8] = set(sig)

        
        for sig in in_s + out:
            if len(sig) == 6:
                chars = set(sig)
                if len(chars.intersection(decode[7])) == 2:
                    decode[6] = set(sig)
                elif len(chars.intersection(decode[4])) == 4:
                    decode[9] = set(sig)
                else :
                    decode[0] = set(sig)
        
        for sig in in_s + out:
            if len(sig) == 5:
                chars = set(sig)
                if len(chars.intersection(decode[7])) == 3:
                    decode[3] = set(sig)
                elif len(chars.intersection(decode[6])) == 5:
                    decode[5] = set(sig)
                else :
                    decode[2] = set(sig)
        
        for j, sig in enumerate(out):
            n = decode_sig(sig, decode)
            ans2 += n*10**(3 - j)



    
    
    print(f'Answer to part 2: {ans2}')
