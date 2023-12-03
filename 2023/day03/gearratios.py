""" Advent of Code 2023 -- Day 03 -- """

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def adj2symb(lines, pos, width):
    N = len(lines)
    M = len(lines[0])

    if pos[0] > 0:
        up = pos[0] - 1
    else :
        up = pos[0]
    if pos[0] < N-1:
        low = pos[0] + 1
    else :
        low = pos[0]
    if pos[1] > 0:
        left = pos[1] - 1
    else :
        left = pos[1]
    if pos[1] + width < M:
        right = pos[1] + width 
    else :
        right = pos[1] + width - 1

    if up != pos[0]:
        for j in range(left, right+1):
            # print(lines[up][j])
            if lines[up][j] != '.':
                # print(up, low, left, right, ':', lines[pos[0]][pos[1]:right])
                return True
    if low != pos[0]:
        for j in range(left, right+1):
            # print(lines[low][j])
            if lines[low][j] != '.':
                # print(up, low, left, right, ':', lines[pos[0]][pos[1]:right])
                return True
    if pos[1] != left:
        # print(lines[pos[0]][left])
        if lines[pos[0]][left] != '.':
            # print(up, low, left, right, ':', lines[pos[0]][pos[1]:right])
            return True
    if pos[1] + width -1 != right:
        # print(lines[pos[0]][right])
        if lines[pos[0]][right] != '.':
            # print(up, low, left, right, ':', lines[pos[0]][pos[1]:right])
            return True
    
    return False


def adj2star(lines, pos, width):
    N = len(lines)
    M = len(lines[0])

    if pos[0] > 0:
        up = pos[0] - 1
    else :
        up = pos[0]
    if pos[0] < N-1:
        low = pos[0] + 1
    else :
        low = pos[0]
    if pos[1] > 0:
        left = pos[1] - 1
    else :
        left = pos[1]
    if pos[1] + width < M:
        right = pos[1] + width 
    else :
        right = pos[1] + width - 1

    if up != pos[0]:
        for j in range(left, right+1):
            # print(lines[up][j])
            if lines[up][j] == '*':
                # print(up, low, left, right, ':', lines[pos[0]][pos[1]:right])
                return True, (up,j)
    if low != pos[0]:
        for j in range(left, right+1):
            # print(lines[low][j])
            if lines[low][j] == '*':
                # print(up, low, left, right, ':', lines[pos[0]][pos[1]:right])
                return True, (low,j)
    if pos[1] != left:
        # print(lines[pos[0]][left])
        if lines[pos[0]][left] == '*':
            # print(up, low, left, right, ':', lines[pos[0]][pos[1]:right])
            return True, (pos[0], left)
    if pos[1] + width -1 != right:
        # print(lines[pos[0]][right])
        if lines[pos[0]][right] == '*':
            # print(up, low, left, right, ':', lines[pos[0]][pos[1]:right])
            return True, (pos[0], right)
    
    return False, (-1, -1)


if __name__ == '__main__':
    
    # Part I    
    data = aoc.get_input('input1.txt')                                  
    # data = aoc.get_input('input2.txt')                                  
    lines = data.splitlines()
    
    # symbols = set()

    # for line in lines:
    #     for c in line:
    #         if c != '.' and c.isnumeric() == False:
    #             symbols.add(c)
    # print(symbols)

    symbols = {'=', '@', '#', '&', '-', '*', '$', '%', '+', '/'}
   
    # extract numbers
    nums = []
    for j, line in enumerate(lines):
        nums.append([])

        nums_pre = line.split('.')
        nums_pre2 = [num for num in nums_pre if num != '']
        

        for num in nums_pre2:
            if num.isdigit():
                nums[j].append(num)
            elif len(num) > 1:
                chars = set()
                for c in num:
                    chars.add(c)
                sep = chars.intersection(symbols)
                
                rm_sep = num.split(sep.pop())
                for string in rm_sep:
                    if len(string) > 0:
                        nums[j].append(string)
    
    N = len(lines)
    M = len(lines[0])

    ans1 = 0

    for j in range(N):
        i = 0
        for num in nums[j]:
            # doublets are possible
            ind = lines[j].index(num, i)
            i = ind+len(num)
            if adj2symb(lines, (j,ind), len(num)):
                ans1 += int(num)

    print(f'Answer to part 1: {ans1}')

    # Part II
    # data = aoc.get_input('input2.txt')
    
    pos_stars = set()
    pos_double = dict()

    for j in range(N):
        i = 0
        for num in nums[j]:
            ind = lines[j].index(num, i)
            i = ind+len(num)
            adj, pos = adj2star(lines, (j,ind), len(num))
            if adj:
                if pos not in pos_stars:
                    pos_stars.add(pos)
                else :
                    pos_double[pos] = []

    for j in range(N):
        i = 0
        for num in nums[j]:
            ind = lines[j].index(num, i)
            i = ind+len(num)
            adj, pos = adj2star(lines, (j,ind), len(num))
            if pos in pos_double.keys():
                pos_double[pos].append(int(num))

    ans2 = 0
    for pos in pos_double.keys():
        if len(pos_double[pos]) != 2:
            print("error:", pos, pos_double[pos])
        ans2 += pos_double[pos][0]*pos_double[pos][1]

    print(f'Answer to part 2: {ans2}')
