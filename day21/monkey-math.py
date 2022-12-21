""" Advent of Code 2022 -- Day 21 -- """

import aoc
# import numpy as np

def parsing(data):
    monkeys = {}
    for line in data.splitlines():
        words = line.split()
        name = words[0].strip(':')
        if words[1].isnumeric():
            # monkey yells a number
            monkeys[name] = int(words[1])
        else :
            op = words[2]
            name1 = words[1]
            name2 = words[3]
            monkeys[name] = (name1, op, name2)
    
    return monkeys

def computing(name, monkeys):
    if name == 'humn':
        return monkeys[name], True
    elif type(monkeys[name]) is int:
        return monkeys[name], False
    else :
        t = monkeys[name]
        z1, h1 = computing(t[0], monkeys)
        z2, h2 = computing(t[2], monkeys)
        if t[1] == '+':
            result = z1 + z2
        if t[1] == '*':
            result = z1 * z2
        if t[1] == '/':
            result = z1 // z2
        if t[1] == '-':
            result = z1 - z2
        return result, h1 or h2

def solving(name, z, monkeys):
    if name == 'humn':
        return z
    else :
        t = monkeys[name]
        z1, h1 = computing(t[0], monkeys)
        z2, h2 = computing(t[2], monkeys)
        if h1:
            if t[1] == '+':
                return solving(t[0], z - z2, monkeys)
            if t[1] == '*':
                return solving(t[0], z // z2, monkeys)
            if t[1] == '/':
                return solving(t[0], z * z2, monkeys)
            if t[1] == '-':
                return solving(t[0], z + z2, monkeys)
        if h2: 
            if t[1] == '+':
                return solving(t[2], z - z1, monkeys)
            if t[1] == '*':
                return solving(t[2], z // z1, monkeys)
            if t[1] == '/':
                return solving(t[2], z1 // z, monkeys)
            if t[1] == '-':
                return solving(t[2], z1 - z, monkeys)

if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    # Part I    
    monkeys = parsing(data)
    result, h = computing('root', monkeys)
    print(f'Part I: root yells {int(result)}')
    
    # Part II
    t = monkeys['root']
    z1, h1 = computing(t[0], monkeys)
    z2, h2 = computing(t[2], monkeys)
    if h1:
        z = solving(t[0], z2, monkeys)
        monkeys['humn'] = int(z)
        z1, h1 = computing(t[0], monkeys)
    else :
        z = solving(t[2], z1, monkeys)
        monkeys['humn'] = int(z)
        z2, h2 = computing(t[2], monkeys)
    
    print(f'Part II: If human = {z} then Root checks if {z1} == {z2}')

