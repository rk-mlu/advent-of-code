""" Advent of Code 2022 -- Day 11 -- """

import aoc

class Monkey:
    def __init__(self, num):
        self.num = num
        self.items = []
        self.icount = 0
        self.operator = None
        self.operand = None
        self.o_divisor = 3
        self.t_divisor = None
        self.targets = None

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
        if wl % self.t_divisor == 0:
            return self.targets[0]
        else :
            return self.targets[1]


if __name__ == '__main__':
    # data = aoc.get_input('input.txt')                                  
    data = aoc.get_input('input2.txt')
    
    # Part I    
    num_rounds = 20
    monkeys = {}
    
    # parsing
    for line in data.splitlines():
        words = line.split()
        if line.startswith('Monkey'):
            num = int(words[-1][:-1])
            M = Monkey(num)
                     
        if line.startswith('  Starting items:'):
            for w in words[2:]:
                M.items.append(int(w.strip(",")))

        if line.startswith('  Operation:'):
            M.operator = words[-2]
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
    num_rounds = 20
    monkeys2 = {}
    
    # parsing
    for line in data.splitlines():
        words = line.split()
        if line.startswith('Monkey'):
            num = int(words[-1][:-1])
            M = Monkey(num)
                     
        if line.startswith('  Starting items:'):
            for w in words[2:]:
                M.items.append(int(w.strip(",")))

        if line.startswith('  Operation:'):
            M.operator = words[-2]
            M.o_divisor = 1
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
            monkeys2[M.num] = M
 
    for r in range(num_rounds):
        print(f'Round {r+1}')
        for m in range(len(monkeys2.keys())):
            M = monkeys2[m]
            for wl in M.items:
                M.icount += 1
                new = M.op(wl)
                tar = M.test(new)
                monkeys2[tar].items.append(new)
            M.items = []
       
        if r in {0, 19, 999, 1999, 2999, 3999}:
            for m in range(len(monkeys2.keys())):
                M = monkeys2[m] 
                print(M, M.icount)

