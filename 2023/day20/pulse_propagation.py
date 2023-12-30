""" Advent of Code 2023 -- Day 20 -- """
year = 2023
day = 20     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    modules = []

    for line in lines:
        i, o = line.split(' -> ')
        if i[0] in ['%', '&']:
            t = i[0]
            lab = i[1:]
        else :
            t = None
            lab = i
        dests = o.split(', ')

        modules.append((lab, t, dests))

    return modules

class ComModule:
    def __init__(self, mod):
        self.lab = mod[0]
        self.type = mod[1]
        self.dests = mod[2]
        self.preds = set()
        
        if self.type == '%':
            self.state = 0
        elif self.type == '&':
            self.state = dict()

    def __str__(self):
        s = f'Node {self.lab} is {self.type}'
        if self.type == 'None':
            s += f' with dests {self.dests}.'
        if self.type == '%':
            s += f' with state {self.state} and dests {self.dests}'
        if self.type == '&':
            s += ' with states '
            for p in self.state.keys():
                s+= f'({p}, {self.state[p]}) '
        return s
    
    def process_pulse(self, orig, hl):
        new_pulses = []
        
        if self.type is None:
            for d in self.dests:
                new_pulses.append((self.lab, d, hl))
                # print(f'{self.lab} {hl} -> {d}')
                
        if self.type == '%':
            if hl == 0:
                self.state = 1 - self.state
                hl_new = self.state
                for d in self.dests:
                    new_pulses.append((self.lab, d, hl_new))
                    # print(f'{self.lab} {hl_new} -> {d}')

        if self.type == '&':
            self.state[orig] = hl

            all_high = 1
            for p in self.preds:
                all_high *= self.state[p]
            if all_high:
                hl_new = 0
            else :
                hl_new = 1

            for d in self.dests:
                new_pulses.append((self.lab, d, hl_new))
                # print(f'{self.lab} {hl_new} -> {d}')

        return new_pulses

def det_preds(network):
    new_nodes = []
    for node in network:
        # print(node)
        for d in network[node].dests:
            if d in network.keys():
                network[d].preds.add(node)
            else :
                new_nodes.append(d)
    for d in new_nodes:
        network[d] = ComModule((d, None, []))

    if len(new_nodes) > 0:
        det_preds(network)

    for node in network:
        if network[node].type == '&':
            for p in network[node].preds:
                network[node].state[p] = 0

def part2(network):
    periods = dict()
    j = 0
    while True:
        Q = [('button', 'broadcaster', 0)]
        j += 1

        while len(Q) > 0:
            pulse = Q.pop(0)

            new_pulses = network[pulse[1]].process_pulse(pulse[0],pulse[2])
            for p in new_pulses:
                if p[0] == 'dh' and p[1] == 'jz' and p[2]==1 and 'dh' not in periods.keys():
                    periods['dh'] = j
                if p[0] == 'mk' and p[1] == 'jz' and p[2]==1 and 'mk' not in periods.keys():
                    periods['mk'] = j
                if p[0] == 'vf' and p[1] == 'jz' and p[2]==1 and 'vf' not in periods.keys():
                    periods['vf'] = j
                if p[0] == 'rn' and p[1] == 'jz' and p[2]==1 and 'rn' not in periods.keys():
                    periods['rn'] = j

            Q = Q + new_pulses
            
        if len(list(periods.keys())) == 4:
            break

    p = 1
    for n in ['dh', 'mk', 'vf', 'rn']:
        p *= periods[n]
            
    return p


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input3.txt')
    
    modules = parsing(data)

    # Part I    

    network = dict()
    for m in modules:
        network[m[0]] = ComModule(m)

    det_preds(network)

    
    num_l = 0
    num_h = 0

    for j in range(1000):
        Q = [('button', 'broadcaster', 0)]

        while len(Q) > 0:
            pulse = Q.pop(0)

            if pulse[2] == 0:
                num_l += 1
            else :
                num_h += 1
            
            Q = Q + network[pulse[1]].process_pulse(pulse[0],pulse[2])
    
    ans1 = num_l*num_h

    print(f'Answer to part 1: {ans1}')

    # Part II
    modules = parsing(data)
    network = dict()
    for m in modules:
        network[m[0]] = ComModule(m)

    det_preds(network)

    ans2 = part2(network)

    print(f'Answer to part 2: {ans2}')
