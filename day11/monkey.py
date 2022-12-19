""" Advent of Code 2022 -- Day 11 -- """

import aoc
import numpy as np

class Monkey:
    def __init__(self, num):
        self.num = num
        self.items = []
        self.items_rk = []
        self.icount = 0
        self.operator = None
        self.operand = None
        self.o_divisor = 3
        self.t_divisor = None
        self.targets = None
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    def __str__(self):
        s = f'Monkey No {self.num}'
        return s

    def op(self, wl):
        if self.operator == '+':
            return (wl + self.operand)//self.o_divisor
        if self.operator == '*':
            return (wl * self.operand)//self.o_divisor
        if self.operator == '**':
            return (wl**2)//self.o_divisor
    
    def test(self, wl):
        # j = self.primes.index(self.t_divisor)
        if wl % self.t_divisor == 0:
            return self.targets[0]
        else :
            return self.targets[1]

    def op_rk(self, wl):
        if self.operator == '+':
            wl_rk = wl + self.operand
        if self.operator == '*':
            wl_rk = wl * self.operand
        if self.operator == '**':
            wl_rk = wl**2

        for j ,p in enumerate(self.primes):
            wl_rk[j] = wl_rk[j] % p

        return wl_rk

    def test_rk(self, wl):
        j = self.primes.index(self.t_divisor)
        if wl[j] == 0:
            return self.targets[0]
        else :
            return self.targets[1]


def parsing(data, odiv=3):
    monkeys = {}
    
    # parsing
    for line in data.splitlines():
        words = line.split()
        if line.startswith('Monkey'):
            num = int(words[-1][:-1])
            M = Monkey(num)
                     
        if line.startswith('  Starting items:'):
            for w in words[2:]:
                
                wl = int(w.strip(","))
                M.items.append(wl)

                wl_rk = np.zeros(len(M.primes), dtype=int)
                for j ,p in enumerate(M.primes):
                    wl_rk[j] = wl % p
                M.items_rk.append(wl_rk)

        if line.startswith('  Operation:'):
            M.operator = words[-2]
            M.o_divisor = odiv
            if words[-1].isnumeric():
                M.operand = int(words[-1])
            else :
                M.operand = 2
                M.operator = '**'
        
        if line.startswith('  Test'):
            M.t_divisor = int(words[-1])

        if line.startswith('    If true:'):
            t1 = int(words[-1])

        if line.startswith('    If false:'):
            t2 = int(words[-1])
            M.targets = (t1, t2)
            monkeys[M.num] = M
    
    return monkeys



if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    # Part I    
    monkeys = parsing(data)
    num_rounds = 20
 
    for r in range(num_rounds):
        print(f'Round {r}')
        for m in range(len(monkeys.keys())):
            M = monkeys[m]
            print(M)
            for wl in M.items:
                M.icount += 1
                new = M.op(wl)
                tar = M.test(new)
                monkeys[tar].items.append(new)
            M.items = []
            print(M.icount)

    # Part II    
    monkeys2 = parsing(data, 1)
    num_rounds = 10000
    
 
    for r in range(num_rounds):
        for m in range(len(monkeys2.keys())):
            M = monkeys2[m]
            for wl in M.items_rk:
                M.icount += 1
                new = M.op_rk(wl)
                tar = M.test_rk(new)
                monkeys2[tar].items_rk.append(new)
            M.items_rk = []
       
        if r in {0, 19, 999, 1999, 2999, 3999, 9999}:
            for m in range(len(monkeys2.keys())):
                M = monkeys2[m] 
                print(M, M.icount)

