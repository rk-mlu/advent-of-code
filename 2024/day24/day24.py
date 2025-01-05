""" Advent of Code 2024 -- Day 24 -- """
year = 2024
day = 24     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    wires = dict()
    out_wires = []
    gates = []

    for line in lines:
        if ':' in line:
            w, v = line.split(':')
            wires[w] = int(v)
        if '->' in line:
            g, tar = line.split(' -> ')
            op1, op, op2 = g.split(' ')
            if op2.startswith('x'):
                gates.append((op, op2, op1, tar))
            else :
                gates.append((op, op1, op2, tar))

            if tar.startswith('z'):
                out_wires.append(tar)


    return wires, gates, set(out_wires)

def part1(wires, gates, outwires):
    ops = {
            'AND': lambda x,y: x & y,
            'OR': lambda x,y: x | y,
            'XOR': lambda x,y: x ^ y
        }

    while len(outwires) > 0:
        
        op, op1, op2, tar = gates.pop(0)
        # print(op, op1, op2, tar)

        v1 = wires.get(op1, -1)
        v2 = wires.get(op2, -1)
        # print(v1, v2)
        if v1 == -1 or v2 == -1:
            gates.append((op, op1, op2, tar))
        else :

            wires[tar] = ops[op](v1,v2)
       
            if tar.startswith('z'):
                outwires.discard(tar)

        # print(wires)

def find_wire(wire, gate):
    out_gates = []
    for g in gates:
        if g[1] == wire or g[2] == wire:
            out_gates.append(g)

    out_gates.sort()
    return out_gates
            


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    wires, gates, out_wires = parsing(data)
    # print(wires)
    # print(gates)
    # print(out_wires)

    # Part I    
    
    part1(wires, gates, out_wires.copy())
    
    M = len(out_wires)
    
    ans1 = 0

    for j in range(M):
        key = f'z{j:02d}'
        ans1 += 2**j*wires[key]

    print(f'Answer to part 1: {ans1}')

    # Part II
    wires, gates, out_wires = parsing(data)
    def my_sort_key(tup):
        return tup[1] + tup[0]
    gates.sort(key=my_sort_key)

    from_xy = []
    for g in gates:
        if g[1].startswith('x'):
            from_xy.append(g[3])
            print(g)
    
    for wire in from_xy:
        g = find_wire(wire, gates)
        print(g)
    
    ## Figured this part out by hand:
    # 1) sort the gates in 
    # 2) output z-- only in XOR Gates
    # 3) except z00, all z-- are never XORed with x-- or y--
    # 4) the result of a x-y XOR is always XORed with the result of OR op from
    #    the previous digit to give z

    ans2 = 'fhc,ggt,hqk,mwh,qhj,z06,z11,z35'
    
    print(f'Answer to part 2: {ans2}')
