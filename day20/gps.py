""" Advent of Code 2022 -- Day 20 -- """

import aoc
# import numpy as np

def parsing(data):
    lines = data.splitlines()
    
    numbers = [ (j,int(n)) for j, n in enumerate(lines)]

    return numbers


def decrypt(numbers):
    N = len(numbers)
    new_numbers = numbers.copy()
    
    # print_numbers(new_numbers)

    for j, n in numbers:
        if n == 0:
            zero = (j,n)
            continue

        k = new_numbers.index((j,n))
        new_numbers.pop(k)

        i = (k + n ) % (N-1)
               
        print(f"{n} moves between {new_numbers[i-1][1]} and {new_numbers[i][1]}:")
        new_numbers.insert(i, (j,n))

        # print_numbers(new_numbers)
            
    return new_numbers, zero

def print_numbers(numbers):
    s = []
    for j, n in numbers:
        s.append(n)
    print(s)

def sum_coord(numbers, zero):

    k = numbers.index(zero)
    print(k)
    
    k1000 = (k + 1000) % N
    k2000 = (k + 2000) % N
    k3000 = (k + 3000) % N
    
    summe = numbers[k1000][1] + numbers[k2000][1] + numbers[k3000][1]
    s = 'Part I: '
    s += f'{numbers[k1000][1]} + {numbers[k2000][1]} + {numbers[k3000][1]}'
    s += f' = {summe}' 

    print(s)



if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    # Part I
    numbers = parsing(data)
    N = len(numbers)

    num_new, zero = decrypt(numbers)

    sum_coord(num_new, zero)

    # Part II
