""" Advent of Code 2023 -- Day 07 -- """

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np
from collections import Counter

def hand2value(hand):
    value = 0
    
    cards = []
    for j in range(2,10):
        cards.append(str(j))
    cards = cards + ['T', 'J', 'Q', 'K', 'A']
    
    b = len(cards)
    p = len(hand)
    
    for e, c in enumerate(hand):
        m = cards.index(c)
        value += m*b**(p-e-1)

    return value

def hand2value2(hand):
    value = 0
    
    cards = []
    for j in range(2,10):
        cards.append(str(j))
    cards = ['J'] + cards + ['T', 'Q', 'K', 'A']
    
    b = len(cards)
    p = len(hand)
    
    for e, c in enumerate(hand):
        m = cards.index(c)
        value += m*b**(p-e-1)

    return value

def hand2type(hand):

    c = Counter(hand)
    max_c = max(c.values())
    num_c = len(c.values())

    if max_c == 5:
        # five of a kind
        return 6
    if max_c == 4:
        # four of a kind
        return 5
    if num_c == 2 and max_c == 3:
        # full house
        return 4
    if num_c == 3 and max_c == 3:
        # three of a kind
        return 3
    if num_c == 3 and max_c == 2:
        # two pairs
        return 2
    if num_c == 4 and max_c == 2:
        # one pair
        return 1
    if num_c == 5:
        return 0

    print(f"error in hand2type({hand})")


def hand2type2(hand):
    
    if hand.count('J') == 0:
        # no joker
        return hand2type(hand)
    
    c = Counter(hand)
    max_c = max(c.values())
    num_c = len(c.values())
    num_J = c['J']


    if max_c >= 4:
        # five of a kind
        return 6
    if num_J == 2 and max_c == 3:
        # five of a kind
        return 6
    if num_J == 3 and num_c == 2:
        # five of a kind
        return 6
    if num_J == 3 and num_c == 3:
        # four of a kind
        return 5
    if num_J == 2 and num_c == 3 and max_c == 2:
        # four of a kind
        return 5
    if num_J == 1 and max_c == 3:
        # four of a kind
        return 5
    if num_J == 1 and num_c == 3 and max_c == 2:
        # full house
        return 4
    if num_J == 1 and num_c == 4 and max_c == 2:
        # three of a kind
        return 3
    if num_J == 2 and num_c == 4:
        # three of a kind
        return 3
    if num_c == 5:
        # one pair
        return 1

    print(f"error in hand2type2({hand})")

def add_rank(hands_type):
    def sort_key(hb):
        return hand2value(hb[0])

    rank = 1
    for t in range(7):
        t_list = hands_type[t]
        t_list.sort(key=sort_key)

        for hb in t_list:
            hb.append(rank)
            rank += 1

def add_rank2(hands_type):
    def sort_key(hb):
        return hand2value2(hb[0])

    rank = 1
    for t in range(7):
        t_list = hands_type[t]
        t_list.sort(key=sort_key)

        for hb in t_list:
            hb.append(rank)
            rank += 1

def total_winnings(hands_type):
    win = 0
    for t in range(7):
        t_list = hands_type[t]

        for hb in t_list:
            win += int(hb[1])*hb[2]
    return win

if __name__ == '__main__':
    data = aoc.get_input('input1.txt')                                  
    # data = aoc.get_input('input2.txt')                                  
    lines = data.splitlines()
    
    list_hands = [line.split() for line in lines]
    
    # Part I    
    hands_type = dict()
    for j in range(7):
        hands_type[j] = []

    for h in list_hands:
        t = hand2type(h[0])
        hands_type[t].append(h)
    
    add_rank(hands_type)

    ans1 = total_winnings(hands_type)

    print(f'Answer to part 1: {ans1}')

    # Part II
    # data = aoc.get_input('input2.txt')
    
    list_hands2 = [line.split() for line in lines]

    hands_type2 = dict()
    for j in range(7):
        hands_type2[j] = []

    for h in list_hands2:
        t = hand2type2(h[0])
        hands_type2[t].append(h)
    
    add_rank2(hands_type2)

    ans2 = total_winnings(hands_type2)
    
    print(f'Answer to part 2: {ans2}')
