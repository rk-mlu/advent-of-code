""" Advent of Code 2022 -- Day 16 -- """

import aoc
import copy
import numpy as np
from itertools import product, chain, pairwise, islice, combinations_with_replacement

class Valve:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        self.connected = {}

    def __str__(self):
        s = f'Valve {self.name} has rate= {self.rate:2d} and is connected to'
        for v in self.connected.keys():
            s+= f' {v, self.connected[v]}'
        return s

def parsing(data):
    valves = {}
    closed = []

    lines = data.splitlines()
    
    for line in lines:
        words = line.split()
        rate = words[4]
        rate = int(rate[5:-1])
        if rate > 0:
            closed.append(words[1])
        v = Valve(words[1], rate)
        for w in words[9:]:
            neighbor = w.strip(',')
            dist = 1
            v.connected[neighbor] = dist
        # print(v)
        valves[words[1]] = v
    
    return valves, closed

def reduce_valves(valves):
    # reduce list of valves by eliminating valves with rate 0 and only 2
    # neighbors
    
    reduced = copy.deepcopy(valves)
    for v in valves.keys():
        if valves[v].rate == 0 and len(valves[v].connected) == 2:
            nbs = list(reduced[v].connected.keys())
            nb1, nb2 = nbs[0], nbs[1]
            reduced[nb1].connected[nb2] = (reduced[v].connected[nb1]
                    + reduced[v].connected[nb2])
            reduced[nb1].connected.pop(v)
            reduced[nb2].connected[nb1] = (reduced[v].connected[nb1] +
                    reduced[v].connected[nb2])
            reduced[nb2].connected.pop(v)
            reduced.pop(v)
    
    print('Reduced network:')
    for v in reduced.keys():
        print(reduced[v])

    return reduced

class Path:
    def __init__(self, start, tlim):
        self.pos = start
        self.hist = [(start, tlim)]
        self.t = tlim
        self.pressure = 0
        self.opened = []
    
    def __str__(self):
        s = f'Pressure released {self.pressure} along the path:'
        for j, (v, m) in enumerate(self.hist):
            s += f'\nMinute {30-m:2}: position {v}'
            if v == self.hist[j-1][0]:
                s+= ' (opened)'
        return s

    def copy(self):
        new_p = Path(self.pos, self.t)
        new_p.hist = copy.deepcopy(self.hist)
        new_p.pressure = self.pressure*1
        new_p.opened = copy.deepcopy(self.opened)
        return new_p

    def remaining(self, valves):
        # crude upper bound for remaing releasable pressure
        r = 0
        rates = []
        for v in valves.keys():
            if v not in self.opened:
                rates.append(valves[v].rate)
        rates = np.array(rates)
        rates.sort()
        tl = np.arange(self.t)
        tl = islice(tl[::-1], 0, None, 3)
        try: 
            for (rate, t) in zip(rates[::-1], tl):
                r += t*rate
        except: 
            print(rates, tl)
        return r

def gen_paths(valves, p, closed, threshold=0):
    max_pressure = max(threshold, p.pressure)
    best_path = p
    
    if p.t == 0:
        return best_path, max_pressure

    if valves[p.pos].rate > 0 and p.pos not in p.opened:
        # check if valve can be opened
        p_op = p.copy()
        p_op.opened.append(p.pos)
        p_op.t -= 1
        p_op.pressure += p_op.t*valves[p.pos].rate
        p_op.hist.append((p.pos, p_op.t))
        
        if len(p_op.opened) == closed:
            return p_op, p_op.pressure
        else :
            p_new, press_new = gen_paths(valves, p_op, closed, max_pressure)
            if press_new > max_pressure:
                max_pressure = press_new
                best_path = p_new
        
    for nb in valves[p.pos].connected.keys():
        if p.t < valves[p.pos].connected[nb]:
            # neighbor nb out of reach
            continue
        if len(p.hist) > 1 and p.hist[-2][0] == nb:
            # do not move hence and forth
            continue
        if len(valves[nb].connected) == 1 and nb in p.opened:
            # do not enter already opened branches
            continue
        p_mv = p.copy()
        p_mv.pos = nb
        p_mv.t = p.t - valves[p.pos].connected[nb]
        p_mv.hist.append((p_mv.pos, p_mv.t))
        
        if p_mv.pressure + p_mv.remaining(valves) > max_pressure:
            # only follow path if remaining pressure is sufficent 
            p_new, press_new = gen_paths(valves, p_mv, closed, max_pressure)
            if press_new > max_pressure:
                max_pressure = press_new
                best_path = p_new

    return best_path, max_pressure

class Path2:
    def __init__(self, start1, start2, tlim):
        self.pos1 = start1
        self.pos2 = start2
        self.hist = [(start1, start2, tlim)]
        self.t = tlim
        self.pressure = 0
        self.opened = []
    
    def __str__(self):
        s = f'Pressure released {self.pressure} along the path:'
        for j, (v1, v2, m) in enumerate(self.hist):
            s += f'\nMinute {26-m:2}: positions {v1, v2}'
            if v1 == self.hist[j-1][0]:
                s+= f' (opened {v1})'
            if v2 == self.hist[j-1][1]:
                s+= f' (opened {v2})'
        return s

    def copy(self):
        new_p = Path2(self.pos1, self.pos2, self.t)
        new_p.hist = copy.deepcopy(self.hist)
        new_p.pressure = self.pressure*1
        new_p.opened = copy.deepcopy(self.opened)
        return new_p

    def remaining(self, valves):
        # crude upper bound for remaing releasable pressure
        r = 0
        rates = []
        for v in valves.keys():
            if v not in self.opened:
                rates.append(valves[v].rate)
        rates = np.array(rates)
        rates.sort()
        rl = islice(pairwise(rates[::-1]), 0, None, 2)
        tl = np.arange(self.t)
        tl = islice(tl[::-1], 0, None, 3)
        for (rate1, rate2), t in zip(rl, tl):
            r += t*(rate1+rate2)
        return r

def gen_paths2(valves, p, closed, threshold=0):
    max_pressure = max(threshold, p.pressure)
    best_path = p
    
    if p.t == 0 or len(p.opened) == closed:
        return best_path, max_pressure
    
    if p.pos1 == p.pos2:
        l1 = chain.from_iterable([[valves[p.pos1].name], valves[p.pos1].connected.keys()])
        it = combinations_with_replacement(l1, 2)
    else :
        l1 = chain.from_iterable([[valves[p.pos1].name], valves[p.pos1].connected.keys()])
        l2 = chain.from_iterable([[valves[p.pos2].name], valves[p.pos2].connected.keys()])
        it = product(l1, l2)

    for nb1, nb2 in it:
        pn = p.copy()
        pn.t = p.t - 1

        if nb1 != p.pos1:
            if len(p.hist) > 1 and p.hist[-2][0] == nb1:
                # do not move hence and forth
                continue
            if len(valves[nb1].connected) == 1 and nb1 in p.opened:
                # do not enter already opened branches
                continue
            pn.pos1 = nb1
        else :
            if valves[p.pos1].rate > 0 and p.pos1 not in p.opened:
                # check if valve can be opened
                pn.opened.append(p.pos1)
                pn.pressure += pn.t*valves[p.pos1].rate
            else :
                continue

        if nb2 != p.pos2:
            if len(p.hist) > 1 and p.hist[-2][1] == nb2:
                # do not move hence and forth
                continue
            if len(valves[nb2].connected) == 1 and nb2 in pn.opened:
                # do not enter already opened branches
                continue
            pn.pos2 = nb2
        else :
            if valves[p.pos2].rate > 0 and p.pos2 not in pn.opened:
                # check if valve can be opened
                pn.opened.append(p.pos2)
                pn.pressure += pn.t*valves[p.pos2].rate
            else :
                continue
            
        pn.hist.append((pn.pos1, pn.pos2, pn.t))

        if pn.pressure + pn.remaining(valves) > max_pressure:
            # only follow path if remaining pressure is sufficent 
            p_new, press_new = gen_paths2(valves, pn, closed, max_pressure)
            if press_new > max_pressure:
                max_pressure = press_new
                best_path = p_new
                print(f'New optimum found with pressure {max_pressure}')
            
    return best_path, max_pressure

if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    # Part I   
    print('Part I: Computing optimal path...')
    valves, closed = parsing(data)
    num_closed = len(closed)
    reduced_valves = reduce_valves(valves)
    
    p = Path('AA', 30)
    p, mp = gen_paths(reduced_valves, p, num_closed)

    print(p)
    print(f'Part I: The most pressure possible to release is {p.pressure}\n')
    
    # Part II
    threshold = 1500
    print('Part II: Computing optimal path...')
    p2 = Path2('AA', 'AA', 26)
    p2, mp2 = gen_paths2(valves, p2, num_closed, 1500)

    print(p2)
    print(f'Part II: The most pressure possible to release is {p2.pressure}')
