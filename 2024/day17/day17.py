""" Advent of Code 2024 -- Day 17 -- """
year = 2024
day = 17     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np
from collections import defaultdict
from itertools import product

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    regs = []
    for k, line in enumerate(lines):
        words = line.split()
        if k < 3:
            regs.append(int(words[-1]))
        if line.startswith('Program'):
            program = [int(n) for n in words[-1].split(',')]
            
    return regs, program

class computer:
    def __init__(self, regs):
        self.pt = 0
        self.A = regs[0]
        self.B = regs[1]
        self.C = regs[2]
        self.out = []
        self.valid = True

    def comboop(self, operand):
        if operand in {0, 1, 2, 3}:
            return operand
        elif operand == 4:
            return self.A
        elif operand == 5:
            return self.B
        elif operand == 6:
            return self.C
        else :
            self.valid = False
            print(f"{operand} is not a valid operand.")

    def instruction(self, opcode, operand):
        if opcode == 0:
            # adv
            self.A = self.A // 2**(self.comboop(operand))
        if opcode == 1:
            # bxl
            self.B = self.B ^ operand
        if opcode == 2:
            # bst
            self.B = self.comboop(operand) % 8
        if opcode == 3:
            # jnz
            if self.A != 0:
                self.pt = operand - 2
        if opcode == 4:
            # bxc
            self.B = self.B ^ self.C
        if opcode == 5:
            # out
            self.out.append(self.comboop(operand) % 8)            
        if opcode == 6:
            # bdv
            self.B = self.A // 2**(self.comboop(operand))
        if opcode == 7:
            # cdv
            self.C = self.A // 2**(self.comboop(operand))
    
    def run(self, program):
        N = len(program)
        
        while self.valid and self.pt < N - 1:
            opcode, operand = program[self.pt], program[self.pt+1]
            # print(opcode, operand)
            self.instruction(opcode, operand)
            self.pt += 2

        # out = "".join([str(n) + ',' for n in self.out[:-1]])
        # out += str(self.out[-1])
        if self.valid:
            return prog2str(self.out)
        else :
            return ""

def prog2str(program):
    out = "".join([str(n) + ',' for n in program[:-1]])
    out += str(program[-1])
    return out

def show_3bits(j):
    bits = []
    while j > 0:
        j, r = divmod(j, 8)
        bits.append(r)
    return bits


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    # data = aoc.get_input('input3.txt')
    
    regs, program = parsing(data)
    
    
    # Part I    
    
    comp = computer(regs)
    ans1 = comp.run(program)

    print(f'Answer to part 1: {ans1}')

    # Part II

    ans2 = set()
    lp = len(program)
    prog = prog2str(program)

    k = 5
    num_bits = 0
    A_list = set([0])

    while k <= lp:
        next_bit = defaultdict(int)
        total = 0
        A_list2 = set()

        for j, A in product(range(8**(k-num_bits)*2**5), A_list):
            regs2 = [A + j*8**num_bits, 0, 0]
            comp2 = computer(regs2)
            out2  = comp2.run(program)

            if out2.startswith(prog[:2*k-1]):
                # print(regs2[0], out2)
                bits = show_3bits(regs2[0])
                next_bit[bits[num_bits]] += 1
                total += 1
                A_list2.add(A)
            if out2 == prog:
                ans2.add(regs2[0])
        
        if len(ans2) > 0:
            break

        cands = next_bit.items()
        cand_bits = []
        for cand in cands:
            if cand[1] > total//10:
                cand_bits.append(cand[0])
        
        A_list_new = set()
    
        for A in A_list2:
            for r in cand_bits:
                A_list_new.add(A + r*8**num_bits)
        
        num_bits += 1
        k += 1
        A_list = A_list_new
        print(k, A_list)

    ans2 = list(ans2)
    ans2.sort()
    
    # verify
    prog = prog2str(program)
    print(f"to find: {prog}")
    regs2 = [ans2[0], 0, 0]
    comp = computer(regs2)
    out = comp.run(program)
    print(out)

    print(f'Answer to part 2: {ans2[0]}')
