""" Advent of Code 2024 -- Day 13 -- """
year = 2024
day = 13     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    rounds = []

    for line in lines:
        if len(line) == 0:
            continue
        if line.startswith('Button A'):
            A = np.zeros((2,2), dtype = int) 
            words = line.split()
            A[0,0] = int(words[2][2:-1])
            A[1,0] = int(words[3][2:])
        if line.startswith('Button B'):
            words = line.split()
            A[0,1] = int(words[2][2:-1])
            A[1,1] = int(words[3][2:])
        if line.startswith('Prize'):
            b = np.zeros((2,1), dtype = int) 
            words = line.split()
            b[0] = int(words[1][2:-1])
            b[1] = int(words[2][2:])
            rounds.append((A,b))

    return rounds

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    machines = parsing(data)

    # Part I

    ans1 = 0
    for A, b in machines:
        det = A[0,0]*A[1,1] - A[0,1]*A[1,0]
        if det == 0:
            print("Matrix is not regular")
            print(A)
            print(b)
        X = A[1,1]*b[0,0] - A[0,1]*b[1,0]
        Y = A[0,0]*b[1,0] - A[1,0]*b[0,0] 
        # print(det, X, Y)
        if X*det < 0 or X % det != 0:
            continue
        if Y*det < 0 or Y % det != 0:
            continue

        X = X // det
        Y = Y // det

        ans1 += 3*X + Y
        

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    
    for A, b in machines:
        det = A[0,0]*A[1,1] - A[0,1]*A[1,0]
        if det == 0:
            print("A is not regular")
            print(A)
            print(b)
        offset = 10000000000000
        X = A[1,1]*(b[0,0] + offset) - A[0,1]*(b[1,0] + offset)
        Y = A[0,0]*(b[1,0] + offset) - A[1,0]*(b[0,0] + offset) 
        if X*det < 0 or X % det != 0:
            continue
        if Y*det < 0 or Y % det != 0:
            continue

        X = X // det
        Y = Y // det

        ans2 += 3*X + Y
    print(f'Answer to part 2: {ans2}')
