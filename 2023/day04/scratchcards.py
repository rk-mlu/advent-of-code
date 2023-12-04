""" Advent of Code 2023 -- Day 04 -- """

import sys
sys.path.append('../../aux')
import aoc
import numpy as np

def parse_cards(lines):
    numbers = dict()
    for line in lines:
        linspl = line.split(':')
        key = linspl[0].split()[1]
        nums = linspl[1].split('|')
        nums[0] = nums[0].split()
        nums[1] = nums[1].split()
        
        numbers[key] = nums

    return numbers

if __name__ == '__main__':
    
    # Part I    
    data = aoc.get_input('input1.txt')                                  
    # data = aoc.get_input('input2.txt')                                  
    lines = data.splitlines()
    
    cards = parse_cards(lines)
    print(cards)
    
    ans1 = 0
    for k in cards.keys():
        winning = set(cards[k][0])
        mynums = set(cards[k][1])

        mywinning = len(mynums.intersection(winning))
        if mywinning > 0:
            ans1 += 2**(mywinning-1)
    
    print(f'Answer to part 1: {ans1}')

    # Part II
    # data = aoc.get_input('input2.txt')

    num_cards = len(lines)
    won_cards = np.ones(num_cards, dtype=int)

    for j,k in enumerate(cards.keys()): 
        winning = set(cards[k][0])
        mynums = set(cards[k][1])

        mywinning = len(mynums.intersection(winning))
        for i in range(mywinning):
            won_cards[j+i+1] += won_cards[j]

    print(won_cards)    
    ans2 = np.sum(won_cards)
    
    print(f'Answer to part 2: {ans2}')
