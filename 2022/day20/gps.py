""" Advent of Code 2022 -- Day 20 -- """

import aoc
# import numpy as np

def parsing(data, key=1):
    lines = data.splitlines()
    
    numbers = [ (j,int(n)*key) for j, n in enumerate(lines)]

    return numbers


def decrypt(numbers, times=1):
    N = len(numbers)
    new_numbers = numbers.copy()
    
    # print_numbers(new_numbers)
    for q in range(times):
        for j, n in numbers:
            if n == 0:
                zero = (j,n)
                continue
    
            k = new_numbers.index((j,n))
            # remove old entry
            new_numbers.pop(k)
            
            # compute new index
            i = (k + n) % (N-1)
                   
            # print(f"{n} moves between {new_numbers[i-1][1]} and {new_numbers[i][1]}:")
            new_numbers.insert(i, (j,n))
    
            # print_numbers(new_numbers)
            
    return new_numbers, zero


def print_numbers(numbers):
    s = []
    for j, n in numbers:
        s.append(n)
    print(s)


def sum_coord(numbers, zero):
    N = len(numbers)
    k = numbers.index(zero)
    
    k1000 = (k + 1000) % N
    k2000 = (k + 2000) % N
    k3000 = (k + 3000) % N
    
    summe = numbers[k1000][1] + numbers[k2000][1] + numbers[k3000][1]

    return summe


if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    # Part I
    numbers = parsing(data)

    num_new, zero = decrypt(numbers)

    summe = sum_coord(num_new, zero)

    s = f'Part I: sum = {summe}' 
    print(s)

    # Part II
    key = 811589153
    rounds = 10
    numbers2 = parsing(data, key)

    num_new2, zero = decrypt(numbers2, rounds)
    summe = sum_coord(num_new2, zero)
    s = f'Part II: sum = {summe}' 
    print(s)
