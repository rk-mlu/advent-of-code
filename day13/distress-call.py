""" Advent of Code 2022 -- Day 13 -- """

import aoc
import ast
# import numpy as np

def parsing(data):
    packets = []

    for j, line in enumerate(data.splitlines()):

        if j % 3 == 2:
            # skip empty line
            continue

        if j % 3 == 0:
            pair = []
            
        pair.append(ast.literal_eval(line))

        if j % 2 == 1:
            packets.append(pair)

    return packets

def compare(p1, p2):

    for d1, d2 in zip(p1, p2):
        if type(d1) is int and type(d2) is int:
            if d1 < d2:
                return True
            elif d1 > d2 :
                return False
            else :
                continue
        if type(d1) is list and type(d2) is list:
            result = compare(d1, d2)
            if result is None:
                continue
            else :
                return result
        if type(d1) is int and type(d2) is list:
            l = []
            l.append(d1)
            result = compare(l, d2)
            if result is None:
                continue
            else :
                return result

        if type(d1) is list and type(d2) is int:
            l = []
            l.append(d2)
            result = compare(d1, l)
            if result is None:
                continue
            else :
                return result

    if len(p1) < len(p2):
        return True
    elif len(p1) > len(p2) :
        return False
    else :
        return None


def bubbleSort(packets):
    # implementation of bubble sort from
    # https://www.geeksforgeeks.org/python-program-for-bubble-sort/
    N = len(packets)
    swapped = False

    for i in range(N - 1):
        for j in range(0, N-i-1):
            if compare(packets[j], packets[j+1]):
                swapped = True
                packets[j], packets[j+1] = packets[j+1], packets[j]
            
        if not swapped:
            return


if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    # Part I    
    packets = parsing(data)
    summe = 0
    for n, pair in enumerate(packets, start=1):
        if compare(pair[0], pair[1]):
            summe += n

    print(f'Part I: sum of indices in right order is {summe}')

    # Part II
    divider = [[[2]], [[6]]]
    packets.append(divider)

    flatpack = [ ]
    for pair in packets:
        flatpack.extend(pair)

    bubbleSort(flatpack)
    flatpack.reverse()
    a = flatpack.index(divider[0]) + 1
    b = flatpack.index(divider[1]) + 1
    print(f'Part II: product of indices is {a * b}')

