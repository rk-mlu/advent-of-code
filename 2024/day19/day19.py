""" Advent of Code 2024 -- Day 19 -- """
year = 2024
day = 19     # set day!

import sys
sys.path.append('../../aux')
import aoc
# import numpy as np

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    prefixes = lines[0].split(', ')
    
    max_l = 0
    for pref in prefixes:
        max_l = max(max_l, len(pref))

    root = make_trie(prefixes)
    
    return max_l, root, lines[2:]

_end = '_'

def make_trie(words):
    root = dict()
    for word in words:
        current_dict = root
        for c in word:
            current_dict = current_dict.setdefault(c, {})
        current_dict[_end] = _end
    return root

def in_trie(trie, word):
    current_dict = trie
    for c in word:
        if c not in current_dict:
            return False
        current_dict = current_dict[c]
    return _end in current_dict

def test_word(word, max_l, trie):
    
    if len(word) == 0:
        return True
    l = min(max_l, len(word))

    while l > 0:
        pref = word[:l]

        if in_trie(trie, pref):
            ans = test_word(word[l:], max_l, trie)
            if ans:
                return True
        l -= 1

    return False

mem = dict()

def test_word2(word, max_l, trie):
    
    if len(word) == 0:
        return 1
    l = min(max_l, len(word))

    ans = 0

    if word in mem:
        return mem[word]

    while l > 0:
        pref = word[:l]
        
        if in_trie(trie, pref):
            n = test_word2(word[l:], max_l, trie)
            mem[word[l:]] = n
            ans += n
        l -= 1

    return ans


if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    max_l, trie, words = parsing(data)

    print(trie)
    # Part I 

    ans1 = 0

    for word in words:
        if test_word(word, max_l, trie):
            ans1 += 1

    print(f'Answer to part 1: {ans1}')

    # Part II
    
    ans2 = 0
    for word in words:
        n = test_word2(word, max_l, trie)
        print(word, n)
        ans2 += n

    print(f'Answer to part 2: {ans2}')
