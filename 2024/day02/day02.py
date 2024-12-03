""" Advent of Code 2024 -- Day XX -- """
year = 2024
day = 2     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    return lines

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    lines = parsing(data)

    reports = []
    
    for line in lines:
        reports.append(np.array([int(n) for n in line.split()], dtype=int))

    # Part I    

    def is_safe(rep):
        ans = True
        
        rep_diff = np.diff(rep)
        maxi = np.max(rep_diff)
        mini = np.min(rep_diff)

        if maxi > 3 or mini < -3:
            ans = False

        if maxi > 0 and mini <= 0:
            ans = False

        if maxi >= 0 and mini < 0:
            ans = False

        return ans


    ans1 = 0

    for rep in reports:
        if is_safe(rep):
            ans1 += 1
        

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0

    for rep in reports:
        if is_safe(rep):
            ans2 += 1
        else:
            n = len(rep)
            for j in range(n):
                mask = [True]*n
                mask[j] = False
                if is_safe(rep[mask]):
                    ans2 += 1
                    break
    
    print(f'Answer to part 2: {ans2}')
