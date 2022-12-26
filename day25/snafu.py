""" Advent of Code 2022 -- Day 25 -- """

import aoc
import math
# import numpy as np

snafu = {
        '0': 0,
        '1': 1,
        '2': 2,
        '-': -1,
        '=': -2
        }

snafurev = {
        '0': (0, '0'),
        '1': (1, '1'),
        '2': (2, '2'),
        '3': (-2, '='),
        '4': (-1, '-')
        }

def snafu2dec(s):
    b = 5
    m = len(s)
    
    dec = 0
    for j in range(m):
        dec += snafu[s[j]]*b**(m - j - 1)

    return dec

def dec2pent(d, padding=0):
    b = 5
    
    p = []
    if d == 0:
        for _ in range(padding+1):
            p.append(0)
        return p
    else :
        e = int(math.log(d)//math.log(b))
    
    if e < padding:
        p.append(0)
        p.extend(dec2pent(d, padding - 1))
    else :
        m = int(d // b**e)
        p.append(m)
        p.extend(dec2pent(d - m*b**e, e-1))

    return p

def pent2snafu(p):
    b = 5
    l = len(p)
    pp = p.copy() 
    s = ''
    for c in range(l,0,-1):
       
        if pp[c-1] > b-1:
            if c == 0:
                pp.insert(0, 0)
            pp[c-2] += pp[c-1] // b
            pp[c-1] = pp[c-1] % b

        m = snafurev[str(pp[c-1])]
        if m[0] < 0:
            if c == 0:
                pp.insert(0, 0)
            pp[c-2] += 1

        s += m[1]

    return s[::-1]

def list2str(p):
    s = ''
    for m in p:
        s += str(m)
    return s

if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    # Part I
    sum_dec = 0
    for line in data.splitlines():
        sum_dec += snafu2dec(line)

    # sum_dec = 25
    p = dec2pent(sum_dec)


    s = pent2snafu(p)
    print(f'Part I: dec {sum_dec} in pent {list2str(p)} in snafu {s}')
    
    
    # Part II
