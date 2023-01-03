""" Advent of Code 2022 -- Day 16 -- """

import aoc
# import numpy as np

class Valve:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        self.connected = []

    def __str__(self):
        s = f'Valve {self.name} has flow rate={self.rate:2d} and is'
        s += f'connected to {self.connected}'
        return s

def parsing(data):
    valves = {}

    lines = data.splitlines()
    
    for line in lines:
        words = line.split()
        rate = words[4]
        rate = int(rate[5:-1])
        v = Valve(words[1], rate)
        for w in words[9:]:
            v.connected.append(w.strip(','))
        print(v)
        valves[words[1]] = v
    
    return valves

if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    # Part I   
    valves = parsing(data)
    
    # Part II
