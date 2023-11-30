""" Advent of Code 2021 -- Day 01 -- """

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

if __name__ == '__main__':
    
    # Part I    
    data = aoc.get_input('input1.txt')                                  

    num_list = [int(line) for line in data.splitlines()]
    
    old_num = num_list[0]
    counter1 = 0

    for num in num_list[1:]:
        if old_num < num:
            counter1 += 1
        old_num = num

    print(f"Answer to part I : {counter1}")
    
    # Part II
    # data = aoc.get_input('input2.txt')
    
    counter2 = 0

    avg_old = num_list[0] + num_list[1] + num_list[2]

    for j in range(len(num_list)-3):
        avg = avg_old - num_list[j] + num_list[j+3]
        if avg > avg_old:
            counter2 += 1
        avg_old = avg

    print(f"Answer to part II: {counter2}")


