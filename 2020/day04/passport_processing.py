""" Advent of Code 2020 -- Day 4 -- """
year = 2020
day = 4     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    return lines

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    lines = parsing(data)

    passports = []
    current = dict()

    for line in lines:
        if len(line) == 0:
            passports.append(current)
            current = dict()
            continue
        else :
            pairs = line.split(" ")
            for pair in pairs:
                k, v = pair.split(':')
                current[k] = v
    # Part I    

    ans1 = 0
    
    necessary = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    print(necessary)
    
    for passp in passports:
        keys = set(passp.keys())
        if necessary.issubset(keys):
            ans1 += 1


    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0

    valid_chars = [str(j) for j in range(10)]
    valid_chars += ['a', 'b', 'c', 'd', 'e', 'f']
    valid_chars = set(valid_chars)
    
    valid_ecl = set("amb blu brn gry grn hzl oth".split())
    
    for passp in passports:

        byr = int(passp.get('byr', 0))
        if byr < 1920 or byr > 2002:
            continue
        
        iyr = int(passp.get('iyr', 0))
        if iyr < 2010 or iyr > 2020:
            continue
        
        eyr = int(passp.get('eyr', 0))
        if eyr < 2020 or eyr > 2030:
            continue
        
        hgt = passp.get('hgt', '0cm')
        if hgt[-2:] == 'cm':
            hgtcm = int(hgt[:-2])
            if hgtcm < 150 or hgtcm > 193:
                continue
        elif hgt[-2:] == 'in':
            hgtcm = int(hgt[:-2])
            if hgtcm < 59 or hgtcm > 76:
                continue
        else : 
            continue

        hcl = passp.get('hcl', '#')
        if hcl[0] != '#' or len(hcl) != 7:
            continue
        else: 
            invalid = False 
            for c in hcl[1:]:
                if c not in valid_chars:
                    invalid = True
            if invalid:
                continue

        ecl = passp.get('ecl', 'X')
        if ecl not in valid_ecl:
            continue
        
        pid = passp.get('pid', '0')
        if len(pid) != 9 or not(pid.isnumeric()):
            continue

        
        print(passp['hgt'])

        ans2 += 1

    
    print(f'Answer to part 2: {ans2}')
